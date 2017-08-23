<template lang="pug">
  v-container(fluid)
    v-layout(row)
      v-flex(xs2 text-xs-center)
        icon(name="user", scale=2, class="login-icon")
      v-flex(xs10)
        v-text-field(
          label="Enter your username"
        )
    v-layout(row)
      v-flex(xs2 text-xs-center)
        icon(name="lock", scale=2, class="login-icon")
      v-flex(xs10)
        v-text-field(
          label="Enter your password"
          v-model="password"
          type="password"
        )
    v-layout(row)
      v-flex(xs12)
        v-btn(block secondary) Login
</template>

<script>
import Icon from 'vue-awesome/components/Icon'

export default {
  data: function () {
    return {
      password: ''
    }
  },
  components: {
    Icon
  }
}
</script>

<style>
.login-icon {
  position: relative;
  top: 40%;
  transform: translateY(-40%);
}
</style>

