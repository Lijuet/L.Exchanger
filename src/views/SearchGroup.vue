<template>
  <div class="gradient-form container-fluid img-background">
    <div class="container py-5 h-100">
      <div class="card border-0 px-5 h-100">
        <div class="serach-part m-5 px-5">
          <h1>Find your study group!!</h1>
          <p class="card-text">
            Choose the language which you want to study and click 'SEARCH'
            button.
          </p>
          <div class="input-group">
            <select
              class="form-select"
              id="inputStudyLanguage"
              v-model="studyLanguage"
            >
              <option selected>Select study language</option>
              <option value="en">English</option>
              <option value="ko">Korean</option>
            </select>
            <button
              class="btn btn-primary border-0 btn-block gradient-custom-2"
              @click="listGroupSearchResult"
            >
              Search Group
            </button>
          </div>
        </div>
        <div class="search-result">
          <div v-for="(group, key) in ableGroups" :key="key">
            <div
              class="
                d-style
                btn btn-brc-tp
                border-2
                bgc-white
                btn-outline-blue btn-h-outline-blue btn-a-outline-blue
                w-100
                my-2
                py-3
                shadow
              "
            >
              <div class="row align-items-center">
                <div class="col-12 col-md-4">
                  <h4 class="fs-3">
                    {{ group.group_name }}
                  </h4>

                  <div>
                    <ul class="widget-user-list">
                      <li>
                        <a href="#"
                          ><img
                            src="https://bootdey.com/img/Content/avatar/avatar7.png"
                            alt=""
                        /></a>
                      </li>
                      <li>
                        <a href="#"
                          ><img
                            src="https://bootdey.com/img/Content/avatar/avatar3.png"
                            alt=""
                        /></a>
                      </li>
                      <li>
                        <a href="#"
                          ><img
                            src="https://bootdey.com/img/Content/avatar/avatar5.png"
                            alt=""
                        /></a>
                      </li>
                      <li class="number"><a href="#">+1</a></li>
                    </ul>
                  </div>
                </div>

                <ul class="list-unstyled mb-0 col-12 col-md-4 my-4 my-md-0">
                  <li>
                    Our study languages are ...
                    <ul>
                      <li
                        v-for="(language, key) in group.study_languages"
                        :key="key"
                      >
                        {{ language }}
                      </li>
                    </ul>
                  </li>
                </ul>

                <div class="col-12 col-md-4 text-center">
                  <div class="">
                    <span class="ml-n15 align-text-bottom fw-bold">
                      Is Recruiting NOW !
                    </span>
                  </div>
                  <a
                    href="#"
                    class="
                      f-n-hover
                      btn btn-primary btn-raised
                      border-0
                      px-4
                      py-25
                      w-75
                      gradient-custom-2
                    "
                  >
                    Join Group
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import store from "@/store";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      studyLanguage: "",
      ableGroups: [],
      wishGroup: "",
    };
  },
  methods: {
    async listGroupSearchResult() {
      const result = await store.dispatch("moduleMatch/searchGroup", {
        studyLanguage: this.studyLanguage,
      });
      this.ableGroups = JSON.parse(result.data["result"]);
    },
  },
});
</script>
<style>
.img-background {
  background-image: url("https://www.teahub.io/photos/full/9-94794_pixels-wallpapers-high-quality-download-free-pixel-art.png");
  background-size: cover;
}
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

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}

.btn:not(:disabled):not(.disabled) {
  cursor: pointer;
}
.btn-a-brc-tp:not(.disabled):not(:disabled).active,
.btn-brc-tp,
.btn-brc-tp:focus:not(:hover):not(:active):not(.active):not(.dropdown-toggle),
.btn-h-brc-tp:hover,
.btn.btn-f-brc-tp:focus,
.btn.btn-h-brc-tp:hover {
  border-color: transparent;
}
.btn-outline-blue {
  color: #0d6ce1;
  border-color: #5a9beb;
  background-color: transparent;
}
.btn {
  cursor: pointer;
  position: relative;
  z-index: auto;
  border-radius: 0.175rem;
  transition: color 0.15s, background-color 0.15s, border-color 0.15s,
    box-shadow 0.15s, opacity 0.15s;
}
.border-2 {
  border-width: 2px !important;
  border-style: solid !important;
  border-color: transparent;
}
.bgc-white {
  background-color: #fff !important;
}

.widget {
  background: #fff;
  margin-bottom: 0.75rem;
  display: block;
  position: relative;
  margin-top: 40px;
}
.widget-user-list > li {
  display: inline-block;
}
.widget-user-list {
  padding: 0;
  list-style-type: none;
}
.widget-user-list {
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
}
.widget-user-list > li + li {
  margin-left: -1.125rem;
}
.widget-user-list > li a {
  display: block;
  border: 0.125rem solid #fff;
  overflow: hidden;
  width: 2.25rem;
  height: 2.25rem;
  margin-bottom: -0.3125rem;
  line-height: 2rem;
  text-align: center;
  text-decoration: none;
  -webkit-border-radius: 2.25rem;
  -moz-border-radius: 2.25rem;
  border-radius: 2.25rem;
}
.widget-user-list > li a img {
  display: block;
  max-width: 100%;
}
.widget-user-list > li.number a {
  background: #c7c7cc;
  color: #fff;
}
.widget-content,
.widget-footer {
  padding: 0.625rem;
  background: #fff;
  position: relative;
}
</style>
