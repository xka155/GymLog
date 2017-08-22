<template>
  <div>
  <template v-if="authenticated">
    <h1>Login</h1>
  </template>
  </div>
</template>

<script>

export default {
  name: 'LoginPage',
  // data: function () {
  //   return { authenticated: false }
  // },
  computed: {
    authenticated: function () {
      return this.$store.state.user.authenticated
    }
  }
}
</script>
