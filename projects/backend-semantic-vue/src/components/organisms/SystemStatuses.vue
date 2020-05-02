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
        <div class="row pb-10">
          <div class="ui segment">
            <div class="ui grid middle aligned">
              <div class="row">
                <div class="six wide column">
                  <h4 class="ui header">Tutor Website</h4>
                </div>
                <div class="four wide column">
                  <p>2 defects</p>
                </div>
                <div class="four wide column">
                  <h3 class="ui header">92.51%</h3>
                </div>
                <div class="two wide column right aligned">
                  <a href="#" @click="toggleVisiblity">{{ defectListDisplayState }}</a>
                </div>
              </div>
              <transition
                enter-active-class="animating in fade down" 
                leave-active-class="animating out fade down">
                <DefectList v-if="isDefectListDisplayVisible"/>
              </transition>
            </div>
          </div>
        </div>
        <div class="row pb-10">
          <div class="ui segment">
            <div class="ui grid middle aligned">
              <div class="row">
                <div class="six wide column">
                  <h4 class="ui header">Tutor Website</h4>
                </div>
                <div class="four wide column">
                  <p>2 defects</p>
                </div>
                <div class="four wide column">
                  <h3 class="ui header">92.51%</h3>
                </div>
                <div class="two wide column right aligned">
                  <a>Expand</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DefectList from "@/components/organisms/DefectList";

export default {
    data() {
        return {
            isDefectListDisplayVisible: true
        }
    },
    computed: {
      defectListDisplayState() {
        return (this.isDefectListDisplayVisible) ? 'Collapse' : 'Expand';
      }
    },
    components: {
        DefectList
    },
    methods: {
      toggleVisiblity() {
        this.isDefectListDisplayVisible = !this.isDefectListDisplayVisible;
      }
    }
};
</script>