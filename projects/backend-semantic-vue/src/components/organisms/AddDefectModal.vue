<template>
  <div>
    <transition 
      enter-active-class="animating fade in" 
      leave-active-class="animating fade out"
      
      @enter="showModal = true"
      >
      <div
        class="ui dimmer modals page transition visible active"
        style="display: flex !important;" v-if="addDefectModalIsOpen"
      >
        <transition
          enter-active-class="animating scale in"
          leave-active-class="animating scale out"
          @leave="addDefectModalIsOpen = false"
        >
          <div class="ui active transition modal" v-if="showModal">
            <div class="header">Add Defect Entry</div>
            <div class="content">
              <form class="ui form">
                <div class="field">
                  <label>Bug Description</label>
                  <textarea name="defect-description" placeholder="Enter description"></textarea>
                </div>
                <div class="fields">
                  <div class="eight wide field">
                    <label>Reported Start Date</label>
                    <input type="date" name="defect-start-date" />
                  </div>
                  <div class="eight wide field">
                    <label>Reported End Date</label>
                    <input type="date" name="defect-end-date" />
                  </div>
                </div>
              </form>
            </div>
            <div class="actions" style="text-align: left;">
              <div class="ui secondary button mr-10">Submit</div>
              <a @click="closeModal" href="#">Cancel</a>
            </div>
          </div>
        </transition>
      </div>
    </transition>
  </div>
</template>

<script>
import { eventBus } from "../../main";

export default {
  data() {
    return {
      addDefectModalIsOpen: {
        type: Boolean,
        default: true
      },
      showModal: {
        type: Boolean,
        default: true
      },
    };
  },
  methods: {
    closeModal() {
      this.showModal = false;
    }
  },
  created() {
    eventBus.$on("addDefectModalWasOpened", value => {
      this.addDefectModalIsOpen = value;
    });
  }
};
</script>