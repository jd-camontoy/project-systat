<template>
  <div>
    <div class="ui two column grid middle aligned">
      <div class="row">
        <div class="column">
          <h3 class="ui header">Current Status</h3>
        </div>
        <div class="column">
          <button class="ui right floated secondary button">Settings</button>
        </div>
      </div>
    </div>

    <div class="ui four column grid">
      <div class="row">
        <app-current-detail-card 
          detail_name="Current Period"
          :detail_value="currentPeriodName" />

        <app-current-detail-card 
          detail_name="Start Date"
          :detail_value="currentPeriodStartDate | formatToProperDate" />

        <app-current-detail-card 
          detail_name="End Date"
          :detail_value="currentPeriodEndDate | formatToProperDate" />
          
        <div class="column">
          <div class="ui card">
            <div class="content">
              <div class="description">
                <span>Expected Uptime (Days)</span>
              </div>
              <div class="header pt-10">183 days</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import PeriodModule from "@/store/modules/period";
import CurrentPeriodDetailCard from "@/components/molecules/CurrentPeriodDetailCard.vue";

@Component({
  components: {
    'app-current-detail-card': CurrentPeriodDetailCard
  },
  filters: {
    formatToProperDate(date: string) {
      const dateObj = new Date(date);
      const formattedDate = 
        dateObj.toLocaleString('default', { month: 'long' }) + ' ' + 
        dateObj.getDate() + ', ' +
        dateObj.getFullYear();
      return formattedDate;
    }
  }
})
export default class CurrentStatuses extends Vue {

  currentPeriodName = "";
  currentPeriodStartDate = 0;
  currentPeriodEndDate = 0;

  mounted() {
    this.initizalizeCurrentPeriod();
  }

  async initizalizeCurrentPeriod(){
    await PeriodModule.initStates();
    const currentPeriod = PeriodModule.getCurrent;
    localStorage.currentPeriodId = currentPeriod.id;
    this.currentPeriodName = currentPeriod.period_name;
    this.currentPeriodStartDate = currentPeriod.period_start_date;
    this.currentPeriodEndDate = currentPeriod.period_end_date;
    console.log('Current period ID initialized. ID is:' + localStorage.currentPeriodId);
  }
  
}
</script>