<template>
  <div>
    <div class="ui two column grid middle aligned">
      <div class="row">
        <div class="column">
          <h3 class="ui header">System Statuses</h3>
        </div>
        <div class="column">
          <button class="ui right floated secondary button">Manage</button>
        </div>
      </div>
    </div>

    <div class="ui grid">
      <div class="sixteen wide column">
        <app-system-detail-card 
          v-for="system in systems"
          :key="system.id"
          :name="system.system_name"
          :defect_count="countDefect(system.defects)"
          :percentage="system.percentage"
          :defects="system.defects" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import SystemModule from "@/store/modules/system";
import SystemDetailCard from '@/components/molecules/SystemDetailCard.vue';
import { Defect } from "@/api/interface";

@Component({
  components: {
    'app-system-detail-card': SystemDetailCard
  }
})
export default class SystemStatuses extends Vue {
  systems = null;

  mounted() {
    this.initializeSystems();
  }

  countDefect(defects: Defect[]) {
    let count = 0;
    for (const defect of defects) {
      count++;
    }
    return count;
  }

  async initializeSystems() {
    await SystemModule.initStates();
    this.systems = SystemModule.currentSystemList;
  }
}
</script>