<template>
  <div v-if="$route.name === 'chatBot'" class="chat-bot-page">
    <section class="heading">
      <h3>AI助手</h3>
      <p> <router-link to="/">首页</router-link> / <span>AI助手</span> </p>
    </section>
    
    <div class="chat-container-wrapper">
      <div class="chat-container">
      <!-- 消息列表 -->
      <div class="messages-container" ref="messagesContainer">
        <div v-for="(message, index) in messages" :key="index" :class="message.type">
          <div class="message-content">
            <div v-if="message.source" class="message-source">{{ message.source }}</div>
            {{ message.content }}
          </div>
        </div>
        
        <div v-if="isTyping" class="typing-indicator">
          <span class="typing-dots">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>
      </div>
      
      <!-- 输入区域 -->
      <div class="input-area">
        <input 
          type="text" 
          v-model="userInput" 
          placeholder="请输入您的问题..."
          class="user-input"
          @keyup.enter="sendMessage"
        >
        <button @click="sendMessage" class="send-btn">
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
      </div>
    </div>
  </div>
  
  <div v-else class="chat-bot-float">
    <div class="chat-bot-trigger" @click="goToChatBot">
      <i class="fas fa-comments"></i>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue'
import axios from 'axios'

// API基础URL - 使用相对路径，让 Nginx 代理处理
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || ''

// 跳转到ChatBot页面
const goToChatBot = () => {
  window.location.href = '/chatBot'
}

// 用户输入内容
const userInput = ref('')

// 消息列表
const messages = ref([
  {
    type: 'bot-message',
    content: '您好！我是湘云绣阁AI助手，很高兴为您提供帮助。\n您可以向我询问关于湘绣的历史、技法、传承人等相关信息。',
    source: ''
  }
])

// 是否正在输入
const isTyping = ref(false)

// 消息容器引用
const messagesContainer = ref(null)

// 发送消息
const sendMessage = () => {
  if (userInput.value.trim() && !isTyping.value) {
    const userMessage = userInput.value.trim()
    
    // 添加用户消息
    messages.value.push({
      type: 'user-message',
      content: userMessage,
      source: ''
    })
    
    // 清空输入框
    userInput.value = ''
    
    // 滚动到底部
    scrollToBottom()
    
    // 获取AI回复
    getAIResponse(userMessage)
  }
}

// 调用后端API获取AI回复
const getAIResponse = async (question) => {
  // 设置正在输入状态
  isTyping.value = true
  
  // 滚动到底部
  nextTick(() => scrollToBottom())
  
  try {
    // 调用后端AI对话接口
    const response = await axios.post(`${API_BASE_URL}/api/chat`, {
      message: question
    })
    
    const { source, answer } = response.data
    
    // 关闭正在输入状态
    isTyping.value = false
    
    // 根据来源显示不同前缀
    let sourceLabel = ''
    if (source === 'keyword_reply') {
      sourceLabel = '🔑 关键词回复'
    } else if (source === 'knowledge_base') {
      sourceLabel = '📚 来自知识库'
    } else if (source === 'deepseek') {
      sourceLabel = '🤖 AI生成回答'
    }
    
    // 添加AI回复
    messages.value.push({
      type: 'bot-message',
      content: answer,
      source: sourceLabel
    })
    
  } catch (error) {
    console.error('获取AI回复失败:', error)
    
    // 错误情况下也关闭输入状态并显示友好提示
    isTyping.value = false
    
    // 获取后端返回的错误信息
    let errorMessage = '抱歉，我暂时无法为您提供回答。'
    if (error.response) {
      // 后端返回了错误响应
      if (error.response.data && error.response.data.error) {
        errorMessage = error.response.data.error
      } else if (error.response.status === 503) {
        errorMessage = 'AI服务未配置，请联系管理员。'
      } else if (error.response.status === 500) {
        errorMessage = '服务器内部错误，请稍后再试。'
      }
    } else if (error.request) {
      // 请求发出但没有收到响应
      errorMessage = '无法连接到服务器，请检查网络或后端服务是否运行。'
    }
    
    messages.value.push({
      type: 'bot-message',
      content: errorMessage,
      source: '❌ 服务异常'
    })
  } finally {
    // 滚动到底部
    nextTick(() => scrollToBottom())
  }
}

// 滚动到底部
const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

// 生命周期钩子
onMounted(async () => {
  console.log('AI助手组件已加载')
  // 滚动到底部
  nextTick(() => scrollToBottom())
})
</script>

<style scoped>
/* 页面样式 */
.chat-bot-page {
  max-width: 1200px;
  margin: 0 auto;
  margin-top: 100px;
  padding-bottom: 50px;
  min-height: calc(100vh - 200px);
}

/* 浮窗样式 */
.chat-bot-float {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 9999;
}

.chat-bot-trigger {
  width: 60px;
  height: 60px;
  background-color: var(--primary-color);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.4rem;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(36, 77, 77, 0.3);
  transition: all 0.3s ease;
}

.chat-bot-trigger:hover {
  background-color: var(--primary-light);
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(36, 77, 77, 0.4);
}

/* 页面标题样式 */
.heading {
  background: var(--primary-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2rem 9%;
  margin-bottom: 0;
  position: relative;
  overflow: hidden;
}

/* 聊天容器包装器 */
.chat-container-wrapper {
  padding: 4rem 9%;
}

.heading::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 100%);
}

.heading h3 {
  font-size: 2.8rem;
  text-transform: uppercase;
  color: #fff;
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 0;
  position: relative;
  z-index: 1;
}

.heading p {
  color: #fff;
  font-size: 1.8rem;
  margin: 0;
  position: relative;
  z-index: 1;
}

.heading p a {
  color: #fff;
  text-decoration: none;
  transition: color 0.3s ease;
}

.heading p a:hover {
  color: var(--warning-color);
  text-decoration: underline;
}

.heading p span {
  color: var(--warning-color);
}



/* 聊天容器 */
.chat-container {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  height: 600px;
}

/* 消息列表 */
.messages-container {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #f9f9f9;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

/* 消息样式 */
.user-message, .bot-message {
  display: flex;
  max-width: 80%;
}

.user-message {
  align-self: flex-end;
}

.bot-message {
  align-self: flex-start;
}

.message-content {
  padding: 12px 16px;
  border-radius: 18px;
  font-size: 1.6rem;
  line-height: 1.5;
  white-space: pre-wrap;
}

.user-message .message-content {
  background-color: var(--primary-color);
  color: #fff;
  border-bottom-right-radius: 6px;
}

.bot-message .message-content {
  background-color: #fff;
  color: #333;
  border-bottom-left-radius: 6px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* 消息来源标签 */
.message-source {
  font-size: 1.2rem;
  color: #244d4d;
  margin-bottom: 6px;
  font-weight: 500;
  opacity: 0.8;
}

.bot-message .message-source {
  color: #244d4d;
}

/* 输入区域 */
.input-area {
  display: flex;
  padding: 20px;
  gap: 10px;
  border-top: 1px solid #eee;
  background-color: #fff;
}

.user-input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid var(--primary-light);
  border-radius: 25px;
  font-size: 1.6rem;
  outline: none;
  transition: all 0.3s ease;
}

.user-input:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(36, 77, 77, 0.1);
}

.send-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: #fff;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  font-size: 1.8rem;
}

.send-btn:hover {
  background-color: var(--primary-light);
  transform: scale(1.05);
}

/* 正在输入指示器 */
.typing-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background-color: #fff;
  border-radius: 18px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.typing-dots span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #999;
  animation: typing 1.4s infinite ease-in-out;
}

.typing-dots span:nth-child(1) {
  animation-delay: -0.32s;
}

.typing-dots span:nth-child(2) {
  animation-delay: -0.16s;
}

@keyframes typing {
  0%, 80%, 100% {
    transform: scale(0.8);
    opacity: 0.5;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .chat-container-wrapper {
    padding: 2rem 5%;
  }
  
  .chat-container {
    height: 500px;
  }
  
  .messages-container {
    padding: 15px;
  }
  
  .input-area {
    padding: 15px;
  }
  
  .message-content {
    font-size: 1.4rem;
    padding: 10px 14px;
  }
}
/* 滚动条样式 */
.messages-container::-webkit-scrollbar {
  width: 6px;
}

.messages-container::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.messages-container::-webkit-scrollbar-thumb {
  background: var(--primary-light);
  border-radius: 3px;
}

.messages-container::-webkit-scrollbar-thumb:hover {
  background: var(--primary-color);
}

/* 响应式设计 - 大屏幕 */
@media (max-width: 1200px) {
  .chat-container-wrapper {
    padding: 3rem 5%;
  }
  
  .heading {
    padding: 2rem 5%;
  }
}

/* 响应式设计 - 平板 */
@media (max-width: 991px) {
  .chat-container {
    height: 450px;
  }
}

/* 响应式设计 - 小手机 */
@media (max-width: 450px) {
  .chat-container {
    height: 400px;
  }
  
  .chat-bot-float {
    bottom: 20px;
    right: 20px;
  }
  
  .chat-bot-trigger {
    width: 50px;
    height: 50px;
    font-size: 2rem;
  }
}
</style>