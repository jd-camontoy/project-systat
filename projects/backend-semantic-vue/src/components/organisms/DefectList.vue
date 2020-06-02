<template>
  <div class="row transition visible">
    <div class="sixteen wide column">
      <table class="ui celled table">
        <thead class="center aligned">
          <tr>
            <th width="35%">Defect Description</th>
            <th width="20%">Reported Start Date</th>
            <th width="20%">Reported End Date</th>
            <th width="15%">Total Defect Downtime (days)</th>
            <th width="10%"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="defect in defects" :key="defect.id">
            <td width="35%" data-label="Defect Description">{{ defect.defect_description }}</td>
            <td width="20%" data-label="Reported Start Date">{{ defect.date_reported }}</td>
            <td width="20%" data-label="Reported End Date">{{ defect.date_fixed_released }}</td>
            <td style="color: red;" width="15%" data-label="Total Defect Downtime (days)">0.01</td>
            <td width="10%" data-label="Actions" class="center aligned">
              <a>Edit</a>
            </td>
          </tr>
        </tbody>
        <tfoot class="full-width">
          <tr>
            <th colspan="5" class="center aligned">
              <div class="ui small secondary button" @click="openAddDefectModal">Add defect</div>
            </th>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<script>
import { eventBus } from '../../main';

export default {
  props: ['defects'],
  methods: {
    openAddDefectModal() {
      eventBus.$emit('addDefectModalWasOpened', true);
    }
  }
}
</script>