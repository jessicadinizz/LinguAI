<template>
  <footer class="footer">
    <div class="footer-container">
      <p class="footer-text">© 2024 LinguaAI. All rights reserved.</p>
      <div class="footer-links">
        <a class="footer-link" href="#">Terms of Service</a>
        <a class="footer-link" href="#">Privacy Policy</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
}
</script>

<style scoped>
.footer {
  padding: 40px 32px;
  border-top: 1px solid #e5e7eb;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: center;
}

.footer-text {
  color: #1e1e1e;
  opacity: 0.6;
  font-size: 14px;
}

.footer-links {
  display: flex;
  gap: 24px;
}

.footer-link {
  color: #1e1e1e;
  opacity: 0.6;
  font-size: 14px;
}

.footer-link:hover {
  opacity: 1;
}
</style>
