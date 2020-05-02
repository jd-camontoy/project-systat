<template>
  <div>
    <div class="ui container">
      <app-header />
      <br />
      <app-current-statuses />
      <br />
      <div class="ui divider"></div>
      <br />
      <app-system-statuses />
    </div>
    <app-add-defect-modal/>
  </div>
</template>

<script>
import Header from "@/components/organisms/Header.vue";
import CurrentStatuses from "@/components/organisms/CurrentStatuses.vue";
import SystemStatuses from "@/components/organisms/SystemStatuses.vue";
import AddDefectModal from "@/components/organisms/AddDefectModal.vue";

export default {
  name: "dashboard",
  components: {
    'app-header': Header,
    'app-current-statuses': CurrentStatuses,
    'app-system-statuses': SystemStatuses,
    'app-add-defect-modal': AddDefectModal
  }
};
</script>