<template>
  <div class="home-container">
    <div class="chat-bot-float">
      <div class="chat-bot-trigger" @click="goToChatBot">
        <i class="fas fa-comments"></i>
      </div>
    </div>
    <section class="heading">
      <h3>首页</h3>
      <p> <router-link to="/" class="active">首页</router-link> </p>
    </section>

    <!-- 首屏展示区域 -->
    <section class="hero">
      <div class="hero-content">
        <h1>湘绣，传承千年的艺术瑰宝</h1>
        <p>探索湘绣的独特魅力，感受传统文化与现代科技的完美融合</p>
        <a href="#first-screen" class="btn">开始探索</a>
      </div>
    </section>

    <!-- 第一屏：定义湘绣 - 文化之根 -->
    <section id="first-screen" class="define-xiangxiu">
      <div class="guofeng-container">
        <div class="guofeng-content">
          <div class="guofeng-header">
            <h2 class="guofeng-title">湘绣文化</h2>
            <div class="title-decoration">
              <span class="decoration-line"></span>
              <span class="decoration-dot">◆</span>
              <span class="decoration-line"></span>
            </div>
          </div>
          <div class="guofeng-text-content">
            <div class="text-section">
              <h3 class="guofeng-subtitle">湘绣是什么？</h3>
              <p class="guofeng-paragraph">湘绣是中国四大名绣之一，起源于湖南长沙，以其精湛的技艺、独特的针法和丰富的题材而闻名于世。</p>
            </div>
            <div class="text-section">
              <h3 class="guofeng-subtitle">为何独特？</h3>
              <ul class="guofeng-list">
                <li class="guofeng-list-item">
                  <span class="list-icon">◈</span>
                  <span class="list-text"><strong>历史悠久</strong>：传承千年，始于汉代，盛于清代</span>
                </li>
                <li class="guofeng-list-item">
                  <span class="list-icon">◈</span>
                  <span class="list-text"><strong>工艺精湛</strong>：以掺针、滚针、网针等特殊针法著称</span>
                </li>
                <li class="guofeng-list-item">
                  <span class="list-icon">◈</span>
                  <span class="list-text"><strong>题材丰富</strong>：涵盖山水、人物、花鸟、走兽等多种题材</span>
                </li>
                <li class="guofeng-list-item">
                  <span class="list-icon">◈</span>
                  <span class="list-text"><strong>文化底蕴</strong>：融合湖湘文化精髓，体现中国传统美学</span>
                </li>
              </ul>
            </div>
            <div class="text-section">
              <p class="guofeng-conclusion">湘绣不仅是一种传统工艺，更是中华民族文化的重要组成部分，承载着深厚的历史文化内涵。</p>
            </div>
          </div>
        </div>
        <div class="guofeng-image">
          <div class="image-frame">
            <img src="../../public/static/pictures/guanyu.png" alt="湘绣文化之根" loading="lazy" class="fade-in">
            <div class="frame-decoration">
              <div class="corner-decoration top-left"></div>
              <div class="corner-decoration top-right"></div>
              <div class="corner-decoration bottom-left"></div>
              <div class="corner-decoration bottom-right"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 第二屏：特色内容展示 - 四大核心支柱 -->
    <section class="core-features">
      <h2 class="guofeng-title">特色内容</h2>
      <p class="section-subtitle">探索湘绣文化的数字化体验之旅</p>
      <div class="features-grid">
        <div class="feature-card book-layout">
          <div class="book-content">
            <div class="content-left">
              <div class="guofeng-header">
                <h3>绣艺典藏</h3>
                <div class="title-decoration">
                  <span class="decoration-line"></span>
                  <span class="decoration-dot">◆</span>
                  <span class="decoration-line"></span>
                </div>
              </div>
              <p class="guofeng-text">针走龙蛇，线舞丹青。千年湘绣，一脉相承，品鉴传世匠心，细览针尖风华。</p>
              <div class="guofeng-features">
                <span class="feature-tag">非遗传承</span>
                <span class="feature-tag">匠心独运</span>
                <span class="feature-tag">文化瑰宝</span>
              </div>
              <router-link to="/exhibition" class="btn guofeng-btn">
                <span class="btn-text">品鉴佳作</span>
              </router-link>
              <router-link to="/models" class="btn guofeng-btn model-btn">
                <span class="btn-text">3D模型展示</span>
              </router-link>
            </div>
            <div class="content-right">
              <div class="book-container guofeng-book">
                <div class="book">
                  <div class="book-page front">
                    <img src="https://pic1.imgdb.cn/item/67fe2d5688c538a9b5d1b565.jpg" alt="湘绣作品" class="book-image">
                    <div class="book-overlay">
                      <span class="book-title">湘绣典藏</span>
                    </div>
                  </div>
                  <div class="book-page back">
                    <img src="https://pic1.imgdb.cn/item/67fe2d5688c538a9b5d1b563.jpg" alt="湘绣作品" class="book-image">
                    <div class="book-overlay">
                      <span class="book-title">匠心之作</span>
                    </div>
                  </div>
                </div>
                <div class="book-ribbon"></div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="feature-card venue-layout">
          <div class="venue-content">
            <div class="venue-left">
              <div class="guofeng-frame">
                <img src="../../public/static/pictures/屏幕截图 2024-05-01 120627.png" alt="数字化展厅" class="venue-image">
                <div class="frame-decoration">
                  <div class="corner top-left"></div>
                  <div class="corner top-right"></div>
                  <div class="corner bottom-left"></div>
                  <div class="corner bottom-right"></div>
                </div>
              </div>
            </div>
            <div class="venue-right">
              <div class="guofeng-header">
                <h3>云游绣馆</h3>
                <div class="title-decoration">
                  <span class="decoration-line"></span>
                  <span class="decoration-dot">◆</span>
                  <span class="decoration-line"></span>
                </div>
              </div>
              <p class="guofeng-text">步入云端绣馆，穿越千年时光。数字化展厅，让传统与现代交相辉映，尽览湘绣艺术之美。</p>
              <div class="guofeng-features">
                <span class="feature-tag">沉浸体验</span>
                <span class="feature-tag">虚实结合</span>
                <span class="feature-tag">文化传承</span>
              </div>
              <router-link to="/venue-exhibition" class="btn guofeng-btn">
                <span class="btn-text">开始漫游</span>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="feature-card collection-layout">
          <div class="collection-content">
            <div class="collection-left">
              <div class="guofeng-header">
                <h3>绣韵藏珍</h3>
                <div class="title-decoration">
                  <span class="decoration-line"></span>
                  <span class="decoration-dot">◆</span>
                  <span class="decoration-line"></span>
                </div>
              </div>
              <p class="guofeng-text">绣韵悠悠，藏珍纳宝。虚拟展馆之中，每一件作品都是时光的见证，文化的传承。</p>
              <div class="guofeng-features">
                <span class="feature-tag">数字藏珍</span>
                <span class="feature-tag">文化积淀</span>
                <span class="feature-tag">艺术传承</span>
              </div>
              <router-link to="/venue-tour" class="btn guofeng-btn">
                <span class="btn-text">探索藏品</span>
              </router-link>
            </div>
            <div class="collection-right">
              <div class="guofeng-image-container">
                <div class="guofeng-frame-decoration">
                  <div class="corner-decoration top-left"></div>
                  <div class="corner-decoration top-right"></div>
                  <div class="corner-decoration bottom-left"></div>
                  <div class="corner-decoration bottom-right"></div>
                  <div class="border-decoration"></div>
                </div>
                <img src="https://pic1.imgdb.cn/item/67fe2d5f88c538a9b5d1b56d.jpg" alt="望月" class="art-image small-image" >
              </div>
            </div>
          </div>
        </div>
        
        <div class="feature-card graph-layout">
          <div class="graph-content">
            <div class="graph-left">
              <div class="guofeng-network">
                <img src="../../public/static/pictures/zhishi.png" alt="智慧图谱" class="graph-image">
                <div class="network-nodes">
                  <div class="node node-1"></div>
                  <div class="node node-2"></div>
                  <div class="node node-3"></div>
                  <div class="node node-4"></div>
                </div>
                <div class="network-lines">
                  <div class="line line-1"></div>
                  <div class="line line-2"></div>
                  <div class="line line-3"></div>
                </div>
              </div>
            </div>
            <div class="graph-right">
              <div class="guofeng-header">
                <h3>绣脉相连</h3>
                <div class="title-decoration">
                  <span class="decoration-line"></span>
                  <span class="decoration-dot">◆</span>
                  <span class="decoration-line"></span>
                </div>
              </div>
              <p class="guofeng-text">千丝万缕，绣脉相连。知识图谱如丝如缕，串联起湘绣文化的点点滴滴，探寻其深层的文化关联。</p>
              <div class="guofeng-features">
                <span class="feature-tag">智慧图谱</span>
                <span class="feature-tag">文化脉络</span>
                <span class="feature-tag">知识传承</span>
              </div>
              <router-link to="/knowledge-graph" class="btn guofeng-btn">
                <span class="btn-text">解锁脉络</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 第三屏：湘绣艺品馆 -->
    <section class="xiangxiu-gallery">
      <div class="gallery-header">
        <h2 class="guofeng-title">湘绣艺品馆</h2>
        <p class="section-subtitle">收藏传世匠心，体验生活美学</p>
        <div class="header-decoration">
          <span class="decorative-line"></span>
          <span class="decorative-dot"></span>
          <span class="decorative-line"></span>
        </div>
      </div>
      
      <!-- 刺绣线迹风格分隔线 -->
      <div class="embroidery-divider">
        <div class="stitch-pattern"></div>
      </div>
      
      <!-- 分区一：传世典藏 | 核心藏品区 -->
      <div class="heritage-collection">
        <div class="collection-header">
          <h3 class="collection-title">非遗湘绣</h3>
          <p class="collection-description">传递收藏与投资价值</p>
          <div class="title-decoration"></div>
        </div>
        
        <div class="heritage-products">
          <div class="heritage-card" @click="goToProduct('马蹄莲')">
            <div class="heritage-image">
              <div class="image-frame">
                <img src="https://pic1.imgdb.cn/item/67fe2d7988c538a9b5d1b579.jpg" alt="马蹄莲" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="heritage-info">
              <h4>马蹄莲</h4>
              <div class="price">¥10.00</div>
              <button class="btn heritage-btn" @click.stop="goToProduct('马蹄莲')">了解详情</button>
            </div>
          </div>
          
          <div class="heritage-card" @click="goToProduct('百花争妍')">
            <div class="heritage-image">
              <div class="image-frame">
                <img src="https://pic1.imgdb.cn/item/67fe2d8788c538a9b5d1b599.jpg" alt="百花争妍" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="heritage-info">
              <h4>百花争妍</h4>
              <div class="price">¥10.00</div>
              <button class="btn heritage-btn" @click.stop="goToProduct('百花争妍')">了解详情</button>
            </div>
          </div>
          
          <div class="heritage-card" @click="goToProduct('饮水虎')">
            <div class="heritage-image">
              <div class="image-frame">
                <img src="https://pic1.imgdb.cn/item/67fe2d5f88c538a9b5d1b56a.jpg" alt="饮水虎" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="heritage-info">
              <h4>饮水虎</h4>
              <div class="price">¥10.00</div> 
              <button class="btn heritage-btn" @click.stop="goToProduct('饮水虎')">了解详情</button>
            </div>
          </div>
        </div>
        
        <div class="more-section">
          <router-link to="/shop" class="btn explore-btn">
            探索非遗商店
            <span class="btn-shine"></span>
          </router-link>
        </div>
      </div>
      
      <!-- 分区二：雅致生活 | 文创周边区 -->
      <div class="elegant-life">
        <div class="collection-header">
          <h3 class="collection-title">雅致周边</h3>
          <p class="collection-description">传递实用与美学</p>
          <div class="title-decoration"></div>
        </div>
        
        <div class="elegant-products">
          <div class="elegant-card" @click="router.push('/peripheral')">
            <div class="elegant-image">
              <div class="image-frame">
                <img src="/static/pictures/丝巾.jpg" alt="湘绣丝巾" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="elegant-info">
              <h4>湘绣丝巾</h4>
              <div class="price">¥398.00</div>
              <button class="btn elegant-btn" @click.stop="router.push('/peripheral')">立即购买</button>
            </div>
          </div>
          
          <div class="elegant-card" @click="router.push('/peripheral')">  
            <div class="elegant-image">
              <div class="image-frame">
                <img src="/static/pictures/书签.jpg" alt="湘绣书签" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="elegant-info">
              <h4>湘绣书签</h4>
              <div class="price">¥88.00</div>
              <button class="btn elegant-btn" @click.stop="router.push('/peripheral')">立即购买</button>
            </div>
          </div>
          
          <div class="elegant-card" @click="router.push('/peripheral')">
            <div class="elegant-image">
              <div class="image-frame">
                <img src="/static/pictures/抱枕.jpg" alt="湘绣抱枕" loading="lazy">
              </div>
              <div class="hover-overlay">
                <span class="view-detail">查看细节</span>
              </div>
            </div>
            <div class="elegant-info">
              <h4>湘绣抱枕</h4>
              <div class="price">¥298.00</div>
              <button class="btn elegant-btn" @click.stop="router.push('/peripheral')">立即购买</button>
            </div>
          </div>
          
        </div>
        
        <div class="elegant-more">
          <router-link to="/peripheral" class="btn elegant-more-btn">
            逛一逛周边商店
            <span class="btn-shine"></span>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// 跳转到ChatBot页面
const goToChatBot = () => {
  router.push('/chatBot')
}

// 跳转到产品详情页面
const goToProduct = (productName) => {
  // 根据产品名称查找对应的产品ID或路由
  const productMap = {
    '马蹄莲': '/product/22',
    '百花争妍': '/product/28', 
    '饮水虎': '/product/8',
  }
  
  const productRoute = productMap[productName] || '/shop'
  router.push(productRoute)
}
</script>

<style scoped>
/* 首页容器样式 - 符合project项目设计 */
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  margin-top: 100px; /* 为固定的导航栏留出空间 */
}

/* 页面标题样式 */
.heading {
  background: var(--primary-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2rem 9%;
  margin-bottom: 3rem;
}

.heading h3 {
  font-size: 2.8rem;
  text-transform: uppercase;
  color: #fff;
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 0;
}

.heading p {
  color: #fff;
  font-size: 1.8rem;
  margin: 0;
}

.heading p a {
  color: #fff;
  text-decoration: none;
}

.heading p a:hover {
  color: var(--warning-color);
}

.heading p span {
  color: var(--warning-color);
}

/* 首屏展示区域样式 */
.hero {
  position: relative;
  min-height: 500px;
  background-image: url('../../public/static/pictures/index.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 4rem;
  padding: 4rem 9%;
  overflow: hidden;
}

/* 背景叠加层，增强文字可读性 */
.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.5));
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  padding: 2rem;
  color: #fff;
}

.hero-content h1 {
  font-size: 4rem;
  margin-bottom: 2rem;
  font-weight: 700;
  line-height: 1.2;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  font-family: 'Noto Serif SC', serif;
  color: #fff;
  /* 明确设置白色字体，确保在任何背景下都清晰可见 */
}

.hero-content p {
  font-size: 1.8rem;
  margin-bottom: 3rem;
  line-height: 1.6;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.hero-content .btn {
  display: inline-block;
  padding: 1rem 3rem;
  font-size: 1.8rem;
  background: rgba(255, 255, 255, 0.95);
  color: var(--primary-color);
  text-decoration: none;
  border-radius: 0;
  transition: all 0.3s ease;
  font-weight: 600;
  border: 2px solid var(--primary-color);
  position: relative;
  overflow: hidden;
  /* 复古风格矩形按钮 */
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
  font-family: 'Noto Serif SC', serif;
}

.hero-content .btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.3));
  z-index: 1;
}

.hero-content .btn span {
  position: relative;
  z-index: 2;
}

.hero-content .btn:hover {
  background: var(--primary-color);
  color: #fff;
  transform: translateY(-2px) translateX(-2px);
  box-shadow: 5px 5px 0 rgba(0, 0, 0, 0.3);
  border-color: #fff;
}

/* 第一屏：定义湘绣样式 - 国风典雅设计 */
.define-xiangxiu {
  padding: 8rem 9%;
  background: linear-gradient(135deg, #f8f9fa 0%, #e8f4f8 50%, #f5f7fa 100%);
  position: relative;
  overflow: hidden;
  border-top: 1px solid rgba(36, 77, 77, 0.1);
  border-bottom: 1px solid rgba(36, 77, 77, 0.1);
}

.define-xiangxiu::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-color), var(--primary-light), var(--primary-color));
}

/* 国风容器样式 */
.guofeng-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  position: relative;
}

.guofeng-container::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(36, 77, 77, 0.05), transparent);
  border-radius: 50%;
  z-index: 0;
}

.guofeng-content {
  position: relative;
  z-index: 1;
}

/* 国风标题样式 */
.guofeng-header {
  text-align: center;
  margin-bottom: 3rem;
  position: relative;
}

.guofeng-title {
  font-size: 3.2rem;
  color: var(--primary-color);
  font-weight: 700;
  font-family: 'Noto Serif SC', serif;
  margin-bottom: 1rem;
  letter-spacing: 0.15em;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.1);
  position: relative;
}

.guofeng-title::before,
.guofeng-title::after {
  content: '◆';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: var(--primary-color);
  font-size: 1.2rem;
  opacity: 0.6;
}

.guofeng-title::before {
  left: -3rem;
}

.guofeng-title::after {
  right: -3rem;
}

/* 标题装饰 */
.title-decoration {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-top: 1rem;
}

.decoration-line {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
}

.decoration-dot {
  color: var(--primary-color);
  font-size: 1.5rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.2); }
}

/* 国风文本内容 */
.guofeng-text-content {
  background: rgba(255, 255, 255, 0.7);
  padding: 2.5rem;
  border-radius: 15px;
  border: 1px solid rgba(36, 77, 77, 0.1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
}

.text-section {
  margin-bottom: 2rem;
  position: relative;
}

.text-section:last-child {
  margin-bottom: 0;
}

/* 国风副标题 */
.guofeng-subtitle {
  font-size: 2rem;
  color: var(--primary-color);
  font-weight: 600;
  margin-bottom: 1rem;
  font-family: 'Noto Serif SC', serif;
  position: relative;
  padding-left: 1.5rem;
}

.guofeng-subtitle::before {
  content: '「';
  position: absolute;
  left: 0;
  top: -0.2rem;
  color: var(--primary-color);
  font-size: 1.5rem;
  opacity: 0.6;
}

.guofeng-subtitle::after {
  content: '」';
  position: absolute;
  right: 0;
  bottom: -0.2rem;
  color: var(--primary-color);
  font-size: 1.5rem;
  opacity: 0.6;
}

/* 国风段落 */
.guofeng-paragraph {
  font-size: 1.6rem;
  color: #555;
  line-height: 1.8;
  text-indent: 2em;
  margin-bottom: 1.5rem;
  font-family: 'Noto Serif SC', serif;
}

/* 国风列表 */
.guofeng-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.guofeng-list-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 8px;
  border-left: 3px solid var(--primary-color);
  transition: all 0.3s ease;
}

.guofeng-list-item:hover {
  background: rgba(36, 77, 77, 0.05);
  transform: translateX(5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.list-icon {
  color: var(--primary-color);
  font-size: 1.2rem;
  margin-right: 1rem;
  margin-top: 0.2rem;
  flex-shrink: 0;
}

.list-text {
  font-size: 1.5rem;
  color: #555;
  line-height: 1.7;
  font-family: 'Noto Serif SC', serif;
}

.list-text strong {
  color: var(--primary-color);
  font-weight: 600;
}

/* 国风结论段落 */
.guofeng-conclusion {
  font-size: 1.6rem;
  color: var(--primary-color);
  line-height: 1.8;
  text-align: center;
  font-style: italic;
  font-family: 'Noto Serif SC', serif;
  padding: 1.5rem;
  background: rgba(36, 77, 77, 0.05);
  border-radius: 10px;
  border: 1px solid rgba(36, 77, 77, 0.1);
  position: relative;
}

.guofeng-conclusion::before {
  content: '“';
  position: absolute;
  top: -0.5rem;
  left: 1rem;
  font-size: 3rem;
  color: var(--primary-color);
  opacity: 0.3;
}

.guofeng-conclusion::after {
  content: '”';
  position: absolute;
  bottom: -0.5rem;
  right: 1rem;
  font-size: 3rem;
  color: var(--primary-color);
  opacity: 0.3;
}

/* 国风图片样式 */
.guofeng-image {
  position: relative;
  z-index: 1;
}

.image-frame {
  position: relative;
  display: inline-block;
  padding: 1.5rem;
  background: linear-gradient(135deg, #fff, #f8f9fa);
  border-radius: 15px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.image-frame img {
  width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.image-frame:hover img {
  transform: scale(1.05);
}

/* 图片框架装饰 */
.frame-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.corner-decoration {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid var(--primary-color);
  opacity: 0.6;
}

.corner-decoration.top-left {
  top: 10px;
  left: 10px;
  border-right: none;
  border-bottom: none;
  border-radius: 5px 0 0 0;
}

.corner-decoration.top-right {
  top: 10px;
  right: 10px;
  border-left: none;
  border-bottom: none;
  border-radius: 0 5px 0 0;
}

.corner-decoration.bottom-left {
  bottom: 10px;
  left: 10px;
  border-right: none;
  border-top: none;
  border-radius: 0 0 0 5px;
}

.corner-decoration.bottom-right {
  bottom: 10px;
  right: 10px;
  border-left: none;
  border-top: none;
  border-radius: 0 0 5px 0;
}

.define-xiangxiu .container {
  display: flex;
  flex-wrap: wrap;
  gap: 4rem;
  align-items: center;
}

.define-xiangxiu .content {
  flex: 1;
  min-width: 300px;
}

.define-xiangxiu .image {
  flex: 1;
  min-width: 300px;
}

.define-xiangxiu .section-title {
  font-size: 3rem;
  color: var(--primary-color);
  margin-bottom: 3rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
}

.define-xiangxiu .section-title span {
  color: #333;
  margin-left: 1rem;
}

.define-xiangxiu .section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 80px;
  height: 4px;
  background: var(--primary-color);
}

.define-xiangxiu .text-content h3 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.define-xiangxiu .text-content p {
  font-size: 1.6rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.define-xiangxiu .text-content ul {
  list-style: none;
  margin-bottom: 2rem;
  padding: 0;
}

.define-xiangxiu .text-content ul li {
  font-size: 1.6rem;
  color: #666;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  position: relative;
  padding-left: 3rem;
  padding: 1.5rem 2rem 1.5rem 3rem;
  background: rgba(249, 249, 249, 0.8);
  border-radius: 0.5rem;
  transition: all 0.3s ease;
  border-left: 4px solid transparent;
}

.define-xiangxiu .text-content ul li:hover {
  background: rgba(240, 240, 240, 0.8);
  transform: translateX(10px);
  border-left: 4px solid var(--primary-color);
}

.define-xiangxiu .text-content ul li::before {
  content: '✦';
  position: absolute;
  left: 1rem;
  color: var(--primary-color);
  font-size: 1.8rem;
  font-weight: bold;
  transition: transform 0.3s ease;
}

.define-xiangxiu .text-content ul li:hover::before {
  transform: scale(1.2) rotate(15deg);
}

.define-xiangxiu .text-content ul li strong {
  color: var(--primary-color);
  font-weight: 600;
  margin-right: 0.5rem;
  font-size: 1.7rem;
}

/* 为列表项添加淡入动画 */
.define-xiangxiu .text-content ul li {
  opacity: 0;
  animation: fadeInUp 0.8s ease forwards;
}

.define-xiangxiu .text-content ul li:nth-child(1) {
  animation-delay: 0.7s;
}

.define-xiangxiu .text-content ul li:nth-child(2) {
  animation-delay: 0.9s;
}

.define-xiangxiu .text-content ul li:nth-child(3) {
  animation-delay: 1.1s;
}

.define-xiangxiu .text-content ul li:nth-child(4) {
  animation-delay: 1.3s;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 国风设计响应式调整 */
@media (max-width: 768px) {
  .define-xiangxiu {
    padding: 4rem 5%;
  }
  
  .guofeng-container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .guofeng-container::before {
    display: none;
  }
  
  .guofeng-title {
    font-size: 2.5rem;
  }
  
  .guofeng-title::before,
  .guofeng-title::after {
    display: none;
  }
  
  .guofeng-text-content {
    padding: 1.5rem;
  }
  
  .guofeng-subtitle {
    font-size: 1.8rem;
  }
  
  .guofeng-subtitle::before,
  .guofeng-subtitle::after {
    display: none;
  }
  
  .guofeng-paragraph {
    font-size: 1.4rem;
  }
  
  .list-text {
    font-size: 1.3rem;
  }
  
  .guofeng-conclusion {
    font-size: 1.4rem;
  }
  
  .guofeng-conclusion::before,
  .guofeng-conclusion::after {
    display: none;
  }
  
  .image-frame {
    padding: 1rem;
  }
}

.define-xiangxiu .image img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease;
}

/* 淡入动画效果 */
.fade-in {
  opacity: 0;
  animation: fadeIn 1.5s ease-in-out forwards;
  animation-delay: 0.5s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.define-xiangxiu .image img:hover {
  transform: scale(1.02);
}

/* 第二屏：四大核心支柱样式 */
.core-features {
  padding: 6rem 9%;
  background-color: #f9f9f9;
  text-align: center;
  position: relative;
}

.core-features::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #fff, var(--primary-color), #fff);
}

.core-features .section-title {
  font-size: 3rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
}

.core-features .section-title span {
  color: #333;
  margin-left: 1rem;
}

.core-features .section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--primary-color);
}

.core-features .section-subtitle {
  font-size: 1.8rem;
  color: #666;
  margin-bottom: 4rem;
  font-weight: 400;
  text-align: center;
}

.core-features .features-grid {
  display: flex;
  flex-direction: column;
  gap: 4rem;
  margin-top: 4rem;
}

.core-features .feature-card {
  flex: 1 1 100%; /* 一排只显示一个卡片 */
  min-width: 100%;
  background: #fff;
  border-radius: 0.5rem;
  text-align: center;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 300px; 
}

/* 线装书布局 */
.core-features .feature-card.book-layout .book-content,
.core-features .feature-card.venue-layout .venue-content,
.core-features .feature-card.graph-layout .graph-content {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  min-height: 280px;
}

/* 缩小的卡片内容区域样式 */
.core-features .feature-card.collection-layout .collection-content {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  min-height: 240px;
}

/* 线装书样式 */
.book-container {
  perspective: 1000px;
  width: 100%;
  max-width: 420px;
  height: 240px;
  transform: scale(1.1);
}

.book {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  animation: bookFlip 8s infinite alternate;
}

.book-page {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  overflow: hidden;
  background: #fff;
}

.book-page.front {
  transform: rotateY(0deg);
}

.book-page.back {
  transform: rotateY(180deg);
}

.book-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@keyframes bookFlip {
  0%, 40% {
    transform: rotateY(0deg);
  }
  60%, 100% {
    transform: rotateY(180deg);
  }
}

.art-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
  transition: transform 0.5s ease;
}

.simple-art:hover .art-image {
  transform: scale(1.05);
}

/* 缩小图片样式 */
.small-image {
  max-width: 80%;
  max-height: 80%;
  object-fit: contain;
  margin: 0 auto;
}

/* 国风图片容器样式 */
.guofeng-image-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(36, 77, 77, 0.05), rgba(36, 77, 77, 0.05));
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* 国风框架装饰 */
.guofeng-frame-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

/* 角落装饰 */
.corner-decoration {
  position: absolute;
  width: 25px;
  height: 25px;
  border: 2px solid white;
  opacity: 0.8;
}

.corner-decoration.top-left {
  top: 10px;
  left: 10px;
  border-right: none;
  border-bottom: none;
  border-radius: 5px 0 0 0;
}

.corner-decoration.top-right {
  top: 10px;
  right: 10px;
  border-left: none;
  border-bottom: none;
  border-radius: 0 5px 0 0;
}

.corner-decoration.bottom-left {
  bottom: 10px;
  left: 10px;
  border-right: none;
  border-top: none;
  border-radius: 0 0 0 5px;
}

.corner-decoration.bottom-right {
  bottom: 10px;
  right: 10px;
  border-left: none;
  border-top: none;
  border-radius: 0 0 5px 0;
}

/* 边框装饰 */
.border-decoration {
  position: absolute;
  top: 25px;
  left: 25px;
  right: 25px;
  bottom: 25px;
  border: 1px solid rgba(36, 77, 77, 0.3);
  border-radius: 5px;
}

/* 悬停效果 */
.guofeng-image-container:hover {
  transform: scale(1.02);
  transition: transform 0.3s ease;
}

@keyframes rotate {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}

@keyframes shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

/* 响应式设计 */
/* 卡片悬停效果 */
.core-features .feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--primary-color);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.core-features .feature-card:hover::before {
  transform: scaleX(1);
}

/* 统一左侧内容区域样式 */
.core-features .feature-card.book-layout .content-left {
  flex: 1;
  min-width: 300px;
  padding: 3rem 2.5rem;
  background: linear-gradient(135deg, #f9f9f9, #fff);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-right: 1px solid #eee;
  min-height: 280px;
}

/* 缩小的左侧内容区域样式 */
.core-features .feature-card.collection-layout .collection-left {
  flex: 1;
  min-width: 300px;
  padding: 2.5rem 2rem;
  background: linear-gradient(135deg, #f9f9f9, #fff);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-right: 1px solid #eee;
  min-height: 240px;
}

/* 统一图片区域样式 */
.core-features .feature-card.book-layout .content-right {
  flex: 1.2;
  min-width: 300px;
  padding: 1.5rem;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 280px;
  overflow: hidden;
}

/* 缩小的图片区域样式 */
.core-features .feature-card.collection-layout .collection-right {
  flex: 1.2;
  min-width: 300px;
  padding: 2rem;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 240px;
  overflow: hidden;
}

/* 统一左侧图片区域样式 */
.core-features .feature-card.venue-layout .venue-left,
.core-features .feature-card.graph-layout .graph-left {
  flex: 1.2;
  min-width: 300px;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2.5rem;
  border-right: 1px solid #eee;
  min-height: 280px;
  overflow: hidden;
}

/* 统一右侧内容区域样式 */
.core-features .feature-card.venue-layout .venue-right,
.core-features .feature-card.graph-layout .graph-right {
  flex: 1;
  min-width: 300px;
  padding: 3rem 2.5rem;
  background: linear-gradient(135deg, #f9f9f9, #fff);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 280px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .core-features {
    padding: 4rem 5%;
  }
  
  .core-features .section-title {
    font-size: 2.5rem;
  }
  
  .core-features .section-subtitle {
    font-size: 1.6rem;
  }
  
  .core-features .feature-card {
    min-height: 260px;
  }
  
  .core-features .feature-card.book-layout .book-content,
  .core-features .feature-card.venue-layout .venue-content,
  .core-features .feature-card.collection-layout .collection-content,
  .core-features .feature-card.graph-layout .graph-content {
    flex-direction: column;
    min-height: 260px;
  }
  
  .core-features .feature-card.book-layout .content-left,
  .core-features .feature-card.venue-layout .venue-right,
  .core-features .feature-card.collection-layout .collection-left,
  .core-features .feature-card.graph-layout .graph-right {
    flex: 1;
    border-right: none;
    border-bottom: 1px solid #eee;
    padding: 2rem 1.5rem;
    min-height: 240px;
    background: linear-gradient(135deg, #f9f9f9, #fff);
  }
  
  .core-features .feature-card.book-layout .content-right,
  .core-features .feature-card.venue-layout .venue-left,
  .core-features .feature-card.collection-layout .collection-right,
  .core-features .feature-card.graph-layout .graph-left {
    flex: 1;
    border-right: none;
    border-bottom: 1px solid #eee;
    padding: 2rem 1.5rem;
    min-height: 240px;
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  }
  
  .core-features .feature-card.book-layout .content-left,
  .core-features .feature-card.venue-layout .venue-right,
  .core-features .feature-card.collection-layout .collection-left,
  .core-features .feature-card.graph-layout .graph-right {
    align-items: center;
    text-align: center;
  }
  
  .core-features .feature-card.book-layout .content-left h3,
  .core-features .feature-card.venue-layout .venue-right h3,
  .core-features .feature-card.collection-layout .collection-left h3,
  .core-features .feature-card.graph-layout .graph-right h3 {
    font-size: 2.2rem;
    min-height: 60px;
  }
  
  .core-features .feature-card.book-layout .content-left p,
  .core-features .feature-card.venue-layout .venue-right p,
  .core-features .feature-card.collection-layout .collection-left p,
  .core-features .feature-card.graph-layout .graph-right p {
    font-size: 1.4rem;
    min-height: 50px;
  }
  
  .core-features .feature-card.book-layout .content-left h3::after,
  .core-features .feature-card.venue-layout .venue-right h3::after,
  .core-features .feature-card.collection-layout .collection-left h3::after,
  .core-features .feature-card.graph-layout .graph-right h3::after {
    left: 50%;
    transform: translateX(-50%);
  }
  
  .core-features .feature-card.book-layout .content-left .btn,
  .core-features .feature-card.venue-layout .venue-right .btn,
  .core-features .feature-card.collection-layout .collection-left .btn,
  .core-features .feature-card.graph-layout .graph-right .btn {
    align-self: center;
  }
  
  .book-container,
  .rotation-container {
    max-width: 300px;
    height: 200px;
  }
}

/* 国风标题样式 */
.guofeng-header {
  text-align: center;
  margin-bottom: 1.5rem;
  position: relative;
}

.guofeng-header h3 {
  font-size: 2.5rem;
  color: var(--primary-color);
  font-weight: 700;
  font-family: 'Noto Serif SC', serif;
  margin-bottom: 0.8rem;
  letter-spacing: 0.1em;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

/* 标题装饰 */
.title-decoration {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.decoration-line {
  width: 40px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
  position: relative;
}

.decoration-line::before,
.decoration-line::after {
  content: '';
  position: absolute;
  width: 6px;
  height: 6px;
  background: var(--primary-color);
  border-radius: 50%;
  top: -2px;
}

.decoration-line::before {
  left: -3px;
}

.decoration-line::after {
  right: -3px;
}

.decoration-dot {
  color: var(--primary-color);
  font-size: 1.2rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

/* 国风文本样式 */
.guofeng-text {
  font-size: 1.6rem;
  color: #444;
  line-height: 1.7;
  text-align: center;
  margin-bottom: 1.5rem;
  font-family: 'Noto Serif SC', serif;
  letter-spacing: 0.05em;
  position: relative;
  padding: 0.8rem 0;
}

.guofeng-text::before,
.guofeng-text::after {
  content: '「';
  position: absolute;
  font-size: 2rem;
  color: var(--primary-color);
  opacity: 0.3;
}

.guofeng-text::before {
  top: 0;
  left: -1rem;
}

.guofeng-text::after {
  content: '」';
  bottom: 0;
  right: -1rem;
}

/* 特色标签 */
.guofeng-features {
  display: flex;
  justify-content: center;
  gap: 0.8rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.feature-tag {
  background: linear-gradient(135deg, rgba(36, 77, 77, 0.1), rgba(36, 77, 77, 0.05));
  color: var(--primary-color);
  padding: 0.6rem 1.2rem;
  border-radius: 20px;
  font-size: 1.3rem;
  font-weight: 500;
  border: 1px solid rgba(36, 77, 77, 0.2);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.feature-tag::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transition: left 0.5s ease;
}

.feature-tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(36, 77, 77, 0.2);
}

.feature-tag:hover::before {
  left: 100%;
}

/* 国风按钮样式 */
.guofeng-btn {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  color: #fff;
  padding: 1.2rem 2.5rem;
  border-radius: 25px;
  font-size: 1.6rem;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: none;
  box-shadow: 0 4px 15px rgba(36, 77, 77, 0.3);
}

.guofeng-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(36, 77, 77, 0.4);
}

.guofeng-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.6s ease;
}

.guofeng-btn:hover::before {
  left: 100%;
}

.model-btn {
  margin-left: 1rem;
  background: linear-gradient(135deg, #4a7c7c, #5a9e9e);
}

.model-btn:hover {
  background: linear-gradient(135deg, #5a9e9e, #6abdbd);
}

.btn-text {
  position: relative;
  z-index: 1;
}



/* 国风书籍装饰 */
.guofeng-book {
  position: relative;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border: 2px solid rgba(36, 77, 77, 0.2);
  border-radius: 10px;
  pointer-events: none;
}

.book-ribbon {
  position: absolute;
  top: -10px;
  right: 20px;
  width: 60px;
  height: 80px;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  clip-path: polygon(0 0, 100% 0, 100% 85%, 50% 100%, 0 85%);
  box-shadow: 0 5px 15px rgba(36, 77, 77, 0.3);
}

.book-ribbon::after {
  content: '绣';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 2rem;
  font-weight: bold;
}

.book-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(36, 77, 77, 0.8), rgba(36, 77, 77, 0.6));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 10px;
}

.book:hover .book-overlay {
  opacity: 1;
}

.book-title {
  color: white;
  font-size: 2rem;
  font-weight: 600;
  text-align: center;
  font-family: 'Noto Serif SC', serif;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* 国风画框装饰 */
.guofeng-frame {
  position: relative;
  display: inline-block;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.frame-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.corner {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid var(--primary-color);
}

.corner.top-left {
  top: 5px;
  left: 5px;
  border-right: none;
  border-bottom: none;
}

.corner.top-right {
  top: 5px;
  right: 5px;
  border-left: none;
  border-bottom: none;
}

.corner.bottom-left {
  bottom: 5px;
  left: 5px;
  border-right: none;
  border-top: none;
}

.corner.bottom-right {
  bottom: 5px;
  right: 5px;
  border-left: none;
  border-top: none;
}


/* 国风网络装饰 */
.guofeng-network {
  position: relative;
  display: inline-block;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.network-nodes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.node {
  position: absolute;
  width: 12px;
  height: 12px;
  background: var(--primary-color);
  border-radius: 50%;
  animation: nodePulse 3s ease-in-out infinite;
}

.node-1 {
  top: 20%;
  left: 20%;
  animation-delay: 0s;
}

.node-2 {
  top: 20%;
  right: 20%;
  animation-delay: 0.5s;
}

.node-3 {
  bottom: 20%;
  left: 20%;
  animation-delay: 1s;
}

.node-4 {
  bottom: 20%;
  right: 20%;
  animation-delay: 1.5s;
}

@keyframes nodePulse {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.7;
  }
}

.network-lines {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.line {
  position: absolute;
  background: linear-gradient(45deg, transparent, var(--primary-color), transparent);
  height: 2px;
  animation: lineFlow 4s ease-in-out infinite;
}

.line-1 {
  top: 25%;
  left: 25%;
  width: 50%;
  transform: rotate(45deg);
  animation-delay: 0s;
}

.line-2 {
  top: 50%;
  left: 20%;
  width: 60%;
  transform: rotate(-45deg);
  animation-delay: 1s;
}

.line-3 {
  top: 75%;
  left: 25%;
  width: 50%;
  transform: rotate(45deg);
  animation-delay: 2s;
}

@keyframes lineFlow {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 1;
  }
}

/* 统一标题下划线样式 */
.core-features .feature-card.book-layout .content-left h3::after,
.core-features .feature-card.venue-layout .venue-right h3::after,
.core-features .feature-card.collection-layout .collection-left h3::after,
.core-features .feature-card.graph-layout .graph-right h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 14px;
  width: 80px;
  height: 4px;
  background: var(--primary-color);
}

/* 统一描述文本样式 */
.core-features .feature-card.book-layout .content-left p,
.core-features .feature-card.venue-layout .venue-right p,
.core-features .feature-card.collection-layout .collection-left p,
.core-features .feature-card.graph-layout .graph-right p {
  font-size: 1.6rem;
  color: #666;
  margin-bottom: 2rem;
  line-height: 1.6;
  min-height: 60px;
  display: flex;
  align-items: center;
}

/* 统一按钮样式 */
.core-features .feature-card.book-layout .content-left .btn,
.core-features .feature-card.venue-layout .venue-right .btn,
.core-features .feature-card.collection-layout .collection-left .btn,
.core-features .feature-card.graph-layout .graph-right .btn {
  align-self: center;
  padding: 0.8rem 2.5rem;
  font-size: 1.4rem;
  background: var(--primary-color);
  color: #fff;
  text-decoration: none;
  border-radius: 0.8rem;
  transition: all 0.3s ease;
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  min-width: 120px;
  margin-bottom: 2rem;
  font-family: "STZhongsong", "SimSun", serif;
  text-align: center;
}

/* 统一按钮悬停样式 */
.core-features .feature-card.book-layout .content-left .btn:hover,
.core-features .feature-card.venue-layout .venue-right .btn:hover,
.core-features .feature-card.collection-layout .collection-left .btn:hover,
.core-features .feature-card.graph-layout .graph-right .btn:hover {
  background: var(--primary-light);
  transform: translateY(-2px) translateX(-2px);
  box-shadow: 5px 5px 0 rgba(0, 0, 0, 0.3);
}

/* 统一图片容器样式 */
.core-features .feature-card.venue-layout .venue-image-container,
.core-features .feature-card.graph-layout .graph-image-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.1);
  position: relative;
}

/* 统一图片容器光效样式 */
.core-features .feature-card.venue-layout .venue-image-container::before,
.core-features .feature-card.graph-layout .graph-image-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: shimmer 3s infinite;
  pointer-events: none;
}

/* 统一图片样式 */
.core-features .feature-card.venue-layout .venue-image,
.core-features .feature-card.graph-layout .graph-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

/* 统一图片悬停效果 */
.core-features .feature-card.venue-layout:hover .venue-image,
.core-features .feature-card.graph-layout:hover .graph-image {
  transform: scale(1.05);
}

.core-features .feature-card .icon-box {
  margin-bottom: 2rem;
  color: var(--primary-color);
  transition: transform 0.3s ease;
  position: relative;
  height: 120px;
  width: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(249, 249, 249, 0.8);
  border-radius: 50%;
  overflow: hidden;
}

.core-features .feature-card .icon-box::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transform: rotate(45deg);
  animation: shine 3s infinite;
}

@keyframes shine {
  0% { transform: translateX(-100%) rotate(45deg); }
  100% { transform: translateX(100%) rotate(45deg); }
}

.core-features .feature-card:hover .icon-box {
  transform: scale(1.1) rotate(5deg);
  background: rgba(230, 230, 230, 0.8);
}

.core-features .feature-card .icon-box i {
  position: relative;
  z-index: 2;
  transition: all 0.3s ease;
}

.core-features .feature-card:hover .icon-box i {
  transform: scale(1.2);
  color: var(--primary-light);
  animation: pulse 1s ease-in-out;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.core-features .feature-card h3 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
  font-weight: 600;
  text-align: center;
}

.core-features .feature-card p {
  font-size: 1.4rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 2rem;
  text-align: center;
  flex: 1;
}

.core-features .feature-card .btn {
  display: inline-block;
  padding: 0.9rem 2.5rem;
  font-size: 1.4rem;
  background: var(--primary-color);
  color: #fff;
  text-decoration: none;
  border-radius: 0;
  transition: all 0.3s ease;
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  margin-top: auto;
}

.core-features .feature-card h3 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.core-features .feature-card p {
  font-size: 1.4rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.core-features .feature-card .btn {
  display: inline-block;
  padding: 0.9rem 2.5rem;
  font-size: 1.4rem;
  background: var(--primary-color);
  color: #fff;
  text-decoration: none;
  border-radius: 0;
  transition: all 0.3s ease;
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}

.core-features .feature-card .btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s ease;
}

.core-features .feature-card .btn:hover::before {
  left: 100%;
}

.core-features .feature-card .btn:hover {
  transform: translateY(-2px) translateX(-2px);
  box-shadow: 5px 5px 0 rgba(0, 0, 0, 0.3);
  background: var(--primary-light);
}

/* 第三屏：湘绣艺品馆样式 */
.xiangxiu-gallery {
  padding: 4rem 9%;
  background-color: #fff;
  text-align: center;
  position: relative;
}

.xiangxiu-gallery::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #fff, var(--primary-color));
}

.gallery-header {
  margin-bottom: 3rem;
  position: relative;
  transition: all 0.5s ease;
}

.gallery-header:hover {
  transform: translateY(-5px);
}

.gallery-header .section-title {
  font-size: 3.2rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.gallery-header .section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--primary-color);
  border-radius: 2px;
  transition: width 0.3s ease;
}

.gallery-header .section-title:hover::after {
  width: 120px;
}

.gallery-header .section-subtitle {
  font-size: 1.8rem;
  color: #666;
  margin-bottom: 2rem;
  font-weight: 400;
}

.header-decoration {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.decorative-line {
  width: 60px;
  height: 1px;
  background: var(--primary-color);
  opacity: 0.6;
}

.decorative-dot {
  width: 8px;
  height: 8px;
  background: var(--primary-color);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.2);
    opacity: 0.8;
  }
}

/* 刺绣线迹风格分隔线 */
.embroidery-divider {
  width: 100%;
  height: 30px;
  margin: 3rem 0;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stitch-pattern {
  width: 80%;
  height: 2px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    var(--primary-color) 25%, 
    transparent 50%, 
    var(--primary-color) 75%, 
    transparent 100%);
  position: relative;
}

.stitch-pattern::before,
.stitch-pattern::after {
  content: '';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 12px;
  height: 12px;
  border: 2px solid var(--primary-color);
  border-radius: 50%;
  background: #fff;
}

.stitch-pattern::before {
  left: -10px;
}

.stitch-pattern::after {
  right: -10px;
}

/* 分区一：传世典藏 | 核心藏品区 */
.heritage-collection {
  background: var(--primary-color);
  padding: 4rem 3rem;
  border-radius: 0.5rem;
  margin-bottom: 4rem;
  color: #fff;
}

.collection-header {
  margin-bottom: 3rem;
  position: relative;
}

.collection-title {
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 0.5rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
}

.heritage-collection .collection-title {
  color: #fff;
}

.collection-description {
  font-size: 1.6rem;
  color: #ccc;
  margin-bottom: 1.5rem;
}

.title-decoration {
  width: 60px;
  height: 2px;
  background: rgba(255, 255, 255, 0.6);
  margin: 0 auto;
  position: relative;
}

.title-decoration::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  background: var(--primary-color);
}

.elegant-life .title-decoration {
  background: rgba(0, 0, 0, 0.3);
}

.elegant-life .title-decoration::before {
  background: #f8f8f8;
  border-color: rgba(0, 0, 0, 0.4);
}

.heritage-products {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: 3rem;
  perspective: 1000px;
}

.heritage-card {
  flex: 1;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 0.5rem;
  overflow: hidden;
  transition: all 0.4s ease;
  backdrop-filter: blur(10px);
  position: relative;
  border: 1px solid rgba(255, 255, 255, 0.3);
  cursor: pointer;
}

.heritage-card:hover {
  transform: translateY(-10px) rotateX(5deg);
  box-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.3);
}

.heritage-image {
  position: relative;
  overflow: hidden;
  height: 240px;
}

.image-frame {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 0.3rem;
}

.image-frame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 1px solid rgba(255, 255, 255, 0.3);
  pointer-events: none;
}

.heritage-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.heritage-card:hover .heritage-image img {
  transform: scale(1.1);
}

.hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: all 0.3s ease;
  backdrop-filter: blur(2px);
}

.heritage-image:hover .hover-overlay {
  opacity: 1;
}

.view-detail {
  color: #fff;
  font-size: 1.4rem;
  font-weight: 600;
  padding: 0.8rem 2rem;
  border: 1px solid #fff;
  border-radius: 25px;
  transition: all 0.3s ease;
}

.view-detail:hover {
  background: #fff;
  color: var(--primary-color);
  transform: scale(1.05);
}

.image-overlay {
  display: none;
}

.heritage-info {
  padding: 1.5rem;
  text-align: center;
  position: relative;
}

.heritage-info::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 2px;
  background: rgba(255, 255, 255, 0.5);
}

.heritage-info h4 {
  font-size: 1.6rem;
  color: #fff;
  margin-bottom: 0.8rem;
  font-weight: 600;
}

.heritage-info .price {
  font-size: 1.4rem;
  color: #fff;
  margin-bottom: 1rem;
  font-weight: 600;
}

.heritage-btn {
  background: transparent;
  border: 1px solid #fff;
  color: #fff;
  padding: 0.7rem 1.8rem;
  font-size: 1.3rem;
  border-radius: 0;
  transition: all 0.3s ease;
  text-align: center;
  display: inline-block;
  min-width: 110px;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.heritage-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
  z-index: -1;
}

.heritage-btn:hover::before {
  left: 0;
}

.heritage-btn:hover {
  background: #fff;
  color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.more-section {
  text-align: center;
  margin-top: 3rem;
  position: relative;
}

.explore-btn {
  background: transparent;
  border: 1px solid #fff;
  color: #fff;
  padding: 1rem 2.5rem;
  font-size: 1.6rem;
  border-radius: 0;
  transition: all 0.3s ease;
  text-align: center;
  display: inline-block;
  min-width: 220px;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.explore-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
  z-index: -1;
}

.explore-btn:hover::before {
  left: 0;
}

.explore-btn:hover {
  background: #fff;
  color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.btn-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 30%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(255, 255, 255, 0.4) 50%, 
    transparent 100%);
  transform: skewX(-20deg);
  transition: left 0.6s ease;
  z-index: -1;
}

.explore-btn:hover .btn-shine {
  left: 130%;
}

.arrow-right {
  margin-left: 0.5rem;
  font-size: 1.4rem;
  transition: all 0.3s ease;
}

.more-link:hover .arrow-right {
  transform: translateX(3px);
}

/* 响应式设计增强 */
@media (max-width: 768px) {
  .gallery-header .section-title {
    font-size: 2.8rem;
  }
  
  .collection-title {
    font-size: 2.2rem;
  }
  
  .header-decoration {
    gap: 0.5rem;
  }
  
  .decorative-line {
    width: 40px;
  }
  
  .stitch-pattern {
    width: 90%;
  }
}

@media (max-width: 450px) {
  .gallery-header .section-title {
    font-size: 2.4rem;
  }
  
  .collection-title {
    font-size: 2rem;
  }
  
  .gallery-header .section-subtitle {
    font-size: 1.6rem;
  }
  
  .header-decoration {
    display: none;
  }
}

/* 分区二：雅致生活 | 文创周边区 */
.elegant-life {
  background: #f8f8f8;
  padding: 4rem 3rem;
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
}

.elegant-life::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    var(--primary-color) 50%, 
    transparent 100%);
}

.elegant-life .collection-title {
  color: var(--primary-color);
}

.elegant-life .collection-description {
  color: #666;
}

.elegant-products {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
  perspective: 1000px;
}

.elegant-card {
  background: #fff;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  transition: all 0.4s ease;
  position: relative;
  border: 1px solid rgba(0, 0, 0, 0.05);
  cursor: pointer;
}

.elegant-card:hover {
  transform: translateY(-10px) rotateX(5deg);
  box-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.15);
}

.elegant-image {
  position: relative;
  overflow: hidden;
  height: 220px;
}

.elegant-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.elegant-card:hover .elegant-image img {
  transform: scale(1.1);
}

.elegant-image:hover .hover-overlay {
  opacity: 1;
}

.elegant-image .image-frame::before {
  border-color: rgba(0, 0, 0, 0.1);
}

.elegant-info {
  padding: 1.5rem;
  text-align: center;
  position: relative;
}

.elegant-info::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 2px;
  background: rgba(0, 0, 0, 0.2);
}

.elegant-info h4 {
  font-size: 1.6rem;
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.elegant-info .price {
  font-size: 1.8rem;
  color: var(--primary-color);
  font-weight: 700;
  margin-bottom: 2rem;
  display: block;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.elegant-btn {
  background: var(--primary-color);
  color: #fff;
  padding: 0.7rem 1.8rem;
  font-size: 1.3rem;
  border-radius: 0;
  transition: all 0.3s ease;
  text-align: center;
  display: inline-block;
  min-width: 110px;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.elegant-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
  z-index: -1;
}

.elegant-btn:hover::before {
  left: 0;
}

.elegant-btn:hover {
  background: var(--primary-light);
  transform: translateY(-2px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
}

.elegant-more {
  text-align: center;
  margin-top: 4rem;
  position: relative;
}

.elegant-more-btn {
  background: var(--primary-color);
  color: #fff;
  padding: 1rem 3rem;
  font-size: 1.6rem;
  border-radius: 0;
  transition: all 0.3s ease;
  text-align: center;
  display: inline-block;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.elegant-more-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
  z-index: -1;
}

.elegant-more-btn:hover::before {
  left: 0;
}

.elegant-more-btn:hover {
  background: var(--primary-light);
  transform: translateY(-2px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
}

.elegant-more-btn:hover .btn-shine {
  left: 130%;
}

/* 响应式设计 */
@media (max-width: 991px) {
  .define-xiangxiu,
  .core-features,
  .xiangxiu-gallery {
    padding: 3rem 5%;
  }
  
  .heading {
    padding: 2rem 5%;
  }
}

@media (max-width: 768px) {
  .heading h3 {
    font-size: 2.4rem;
  }
  
  .heading p {
    font-size: 1.6rem;
  }
  
  .define-xiangxiu .container {
    flex-direction: column;
    text-align: center;
  }
  
  .define-xiangxiu .content,
  .define-xiangxiu .image {
    flex: 1;
  }
  
  .define-xiangxiu .section-title::after,
  .core-features .section-title::after,
  .featured-products .section-title::after {
    left: 50%;
    transform: translateX(-50%);
  }
  
  .core-features .features-grid,
  .elegant-products {
    grid-template-columns: 1fr;
  }
  
  .heritage-products {
    flex-direction: column;
  }
  
  .define-xiangxiu .text-content ul li {
    text-align: left;
  }
  
  .heritage-info,
  .elegant-info {
    text-align: center;
  }
  
  .heritage-btn,
  .elegant-btn {
    margin: 0 auto;
  }
  
  .define-xiangxiu .section-title,
  .core-features .section-title,
  .gallery-header .section-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 450px) {
  .heading h3 {
    font-size: 2rem;
  }
  
  .define-xiangxiu,
  .core-features,
  .xiangxiu-gallery {
    padding: 3rem 5%;
  }
  
  .heritage-collection,
  .elegant-life {
    padding: 3rem 2rem;
  }
  
  .heritage-image {
    height: 200px;
  }
  
  .elegant-image {
    height: 180px;
  }
}
  
  .define-xiangxiu .text-content h3 {
    font-size: 1.8rem;
  }
  
  .define-xiangxiu .text-content p,
  .define-xiangxiu .text-content ul li {
    font-size: 1.4rem;
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

/* 响应式设计 - 小手机 */
@media (max-width: 450px) {
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