<template>
  <div class="gradient-form container-fluid img-background">
    <section class="cotainer py-5 h-100">
      <div class="container">
        <div class="card-deck row justify-content-around">
          <div class="col-xs-12 col-sm-6 col-md-4">
            <div class="card border-0 h-100">
              <div class="view overlay">
                <img
                  class="card-img-top"
                  src="https://mdbootstrap.com/img/Photos/Others/images/16.jpg"
                  alt="Card image cap"
                />
                <a href="#!">
                  <div class="mask rgba-white-slight"></div>
                </a>
              </div>

              <div class="card-body">
                <h4 class="card-title" :style="{ color: 'red' }">
                  Make New Study Group
                </h4>
                <p class="card-text">
                  Is there any study group <br />
                  you're looking for? <br />
                  <b> Create your own study group. </b>
                </p>
                <button
                  type="button"
                  class="
                    btn btn-primary
                    border-0
                    btn-block
                    fa-lg
                    gradient-custom-2
                    mb-3
                  "
                  @click="
                    $router.push({
                      path: 'makegroup',
                    })
                  "
                >
                  CREATE
                </button>
              </div>
            </div>
          </div>
          <div class="col-xs-12 col-sm-6 col-md-4">
            <div class="card border-0">
              <div class="view overlay">
                <img
                  class="card-img-top"
                  src="https://mdbootstrap.com/img/Photos/Others/images/15.jpg"
                  alt="Card image cap"
                />
                <a href="#!">
                  <div class="mask rgba-white-slight"></div>
                </a>
              </div>
              <div class="card-body">
                <h4 class="card-title" :style="{ color: 'red' }">
                  Search Study Group
                </h4>
                <p class="card-text">
                  Don't you have a study group yet? <br />
                  <b>
                    Find the right study group for you <br />
                    with just one click.
                  </b>
                </p>
                <button
                  type="button"
                  class="
                    btn btn-primary
                    border-0
                    btn-block
                    fa-lg
                    gradient-custom-2
                    mb-3
                  "
                  @click="
                    $router.push({
                      path: 'searchgroup',
                    })
                  "
                >
                  FIND
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import store from "@/store";
import { defineComponent } from "vue";
import { mapState, mapMutations, mapActions } from "vuex";

export default defineComponent({
  name: "Home",
  data() {
    return {
      studyLanguage: "",
      ableMembers: [],
      wishMembers: [],
    };
  },
  computed: {
    ...mapState("moduleURL", ["backBaseURL"]),
    ...mapState("moduleUser", ["userEmail"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
    ...mapActions("moduleMatch", ["makeStudyGroup"]),
    async listAutoMatchResult() {
      const result = await store.dispatch("moduleMatch/autoMatchGroup", {
        studyLanguage: this.studyLanguage,
      });
      this.ableMembers = JSON.parse(result.data["result"]);
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
</style>
