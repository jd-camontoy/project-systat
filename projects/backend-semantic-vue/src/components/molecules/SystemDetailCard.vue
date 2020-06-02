<template>
    <div class="row pb-10">
        <div class="ui segment">
            <div class="ui grid middle aligned">
                <div class="row">
                    <div class="six wide column">
                        <h4 class="ui header">{{ name }}</h4>
                    </div>
                    <div class="four wide column">
                        <p>{{ defect_count }} defects</p>
                    </div>
                    <div class="four wide column">
                        <h3 class="ui header">{{ percentage }}%</h3>
                    </div>
                    <div class="two wide column right aligned">
                        <a href="#" @click="toggleVisiblity">{{ defectListDisplayState }}</a>
                    </div>
                </div>
                <transition
                    enter-active-class="animating in fade down" 
                    leave-active-class="animating out fade down">
                    <app-defect-list 
                        v-if="isDefectListDisplayVisible"
                        :defects="defects"/>
                </transition>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import DefectList from "@/components/organisms/DefectList.vue";

@Component({
  components: {
    'app-defect-list': DefectList
  },
  props: ['name', 'defect_count', 'percentage', 'defects']
})
export default class SystemDetailCard extends Vue {
  isDefectListDisplayVisible = false;

  get defectListDisplayState() {
    return (this.isDefectListDisplayVisible) ? 'Collapse' : 'Expand';
  }

  toggleVisiblity() {
    this.isDefectListDisplayVisible = !this.isDefectListDisplayVisible;
  }
}
</script>