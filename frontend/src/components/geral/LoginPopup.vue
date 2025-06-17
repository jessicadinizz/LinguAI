<template>
  <div class="popup-overlay">
    <div class="popup">
      <h3 class="popup-title">Please log in or sign up</h3>
      <p class="popup-description">You need to be logged in to use this feature.</p>
      <div class="popup-actions">
        <router-link to="/login" class="popup-link">Log in</router-link>
        <router-link to="/cadastro" class="popup-signup">Sign up</router-link>
      </div>
      <button @click="closePopup" class="popup-close">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPopup',
  methods: {
    closePopup() {
      this.$emit('close-popup')
    },
  },
}
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup {
  background-color: white;
  padding: 24px;
  border-radius: 12px;
  max-width: 400px;
  width: 100%;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.popup-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 12px;
}

.popup-description {
  font-size: 16px;
  margin-bottom: 24px;
}

.popup-actions {
  display: flex;
  justify-content: space-around;
  gap: 12px;
}

.popup-link,
.popup-signup {
  text-decoration: none;
  color: #ad46ff;
  font-weight: bold;
  padding: 10px 20px;
  border-radius: 8px;
  background-color: #ad46ff;
  color: white;
  font-size: 16px;
  transition: background-color 0.3s;
}

.popup-link:hover,
.popup-signup:hover {
  background-color: #8c2ee6;
}

.popup-close {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.popup-close:hover {
  background-color: #e11b1b;
}
</style>
