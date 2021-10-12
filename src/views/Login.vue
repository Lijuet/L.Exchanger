<template>
  <section class="gradient-form img-background">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-xl-10">
          <div class="card border-0 rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-6">
                <div class="card-body p-md-5 mx-md-4">
                  <div class="text-center">
                    <img
                      src="../assets/img/logo.png"
                      style="width: 185px"
                      alt="logo"
                    />
                    <h4 class="mt-1 mb-5 pb-1">Jump to the L.Exchanger</h4>
                  </div>

                  <form>
                    <label class="form-label" for="email">Email</label>
                    <div class="form-outline mb-4">
                      <input
                        id="signinEmail"
                        type="email"
                        v-model="email"
                        class="form-control"
                        placeholder="Email address"
                      />
                    </div>

                    <div class="form-outline mb-4">
                      <label class="form-label" for="signinPassword">
                        Password
                      </label>
                      <input
                        id="signinPassword"
                        type="password"
                        v-model="password"
                        class="form-control"
                      />
                    </div>

                    <div class="text-center pt-1 mb-5 pb-1">
                      <button
                        class="
                          btn btn-primary
                          border-0
                          btn-block
                          fa-lg
                          gradient-custom-2
                          mb-3
                        "
                        type="button"
                        @click="
                          login({ email: this.email, password: this.password })
                        "
                      >
                        Log in
                      </button>
                      <!-- <a class="text-muted" href="#!">Forgot password?</a> -->
                    </div>

                    <div
                      class="
                        d-flex
                        align-items-center
                        justify-content-center
                        pb-4
                      "
                    >
                      <p class="mb-0 me-2">Don't have an account?</p>
                      <button
                        type="button"
                        class="btn btn-outline-danger"
                        @click="signup"
                      >
                        Create new
                      </button>
                    </div>
                  </form>
                </div>
              </div>
              <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                  <h4 class="mb-4">We are more than just a company</h4>
                  <p class="small mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";

export default defineComponent({
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions("moduleUser", ["login"]),
    signup() {
      this.$router.push({ name: "SignUp" });
    },
  },
});
</script>
<style>
.gradient-custom-2 {
  /* fallback for old browsers */
  background: #fccb90;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    #ee7724,
    #d8363a,
    #dd3675,
    #b44593
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

.img-background {
  background-image: url("https://www.teahub.io/photos/full/9-94794_pixels-wallpapers-high-quality-download-free-pixel-art.png");
  background-size: cover;
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}
@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}
</style>
