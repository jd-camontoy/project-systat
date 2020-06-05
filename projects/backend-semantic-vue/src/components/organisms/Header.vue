<template>
  <div class="ui menu mt-10">
    <a href="#" class="header item">
      <img class="ui logo fluid" :src="LogoURL" />
    </a>
    <div class="right menu">
      <div class="ui simple dropdown item">
        <img class="ui avatar image" :src="UserAvatarURL" />
        Username
        <i class="dropdown icon"></i>
        <div class="menu">
          <a class="item" href="#">Account Settings</a>
          <a class="item" href="#">Logout</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LogoURL from "@/assets/images/logo.png"
import UserAvatarURL from "@/assets/images/square-image.png"

export default {
    data() {
        return {
            LogoURL,
            UserAvatarURL
        }
    }
}
</script>