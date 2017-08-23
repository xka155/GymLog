<template>
  <div id="login-wrapper">
    <template v-if="!authenticated">
      <main>
        <div class="hidden-sm-and-down" id="desktop-login">
          <v-container fluid fill-height>
            <v-layout flex align-center justify-center>
              <v-card class="grey lighten-4" id="login-card">
                <login-form></login-form>
              </v-card>
            </v-layout>
          </v-container>
        </div>
      </main>
    </template>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'

export default {
  name: 'LoginPage',
  computed: {
    authenticated: function () {
      return this.$store.state.user.authenticated
    }
  },
  components: {
    LoginForm
  }
}
</script>

<<style>
  #desktop-login {
    padding-top: 25vh;
    padding-bottom: 25vh
  }

  #login-card {
    width: 60vh
  }
</style>
