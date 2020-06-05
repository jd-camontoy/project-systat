<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "app",
  components: {}
});
</script>

<style>
  @import "~@/assets/semantic/semantic.min.css";
  @import "~@/assets/custom-css/padding.css";
</style>