<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid px-3">
      <!-- Avatar -->
      <div class="d-flex align-items-center">
        <img
          src="https://bootdey.com/img/Content/avatar/avatar7.png"
          class="rounded-circle"
          height="28"
          alt=""
          loading="lazy"
        />
        <div class="row">
          <span :style="{ fontSize: '18px', color: 'black' }">
            <b> Level 10 </b> | Next Level
          </span>
          <img class="mx-1" src="../../assets/img/energyBar.png" height="22" />
        </div>
      </div>
      <button type="button" class="btn btn-outline-danger" @click="removeToken">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-power"
          viewBox="0 0 16 16"
        >
          <path d="M7.5 1v7h1V1h-1z"></path>
          <path
            d="M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z"
          ></path>
        </svg>
      </button>
    </div>
  </nav>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { mapMutations } from "vuex";

export default defineComponent({
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
  },
});
</script>
