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
        <div class="column">
          <div class="ui card">
            <div class="content">
              <div class="description">
                Current Period
                <a class="right floated">Change</a>
              </div>
              <div class="header pt-10">2nd Half 2020</div>
            </div>
          </div>
        </div>
        <div class="column">
          <div class="ui card">
            <div class="content">
              <div class="description">
                Start Date
                <a class="right floated">Change</a>
              </div>
              <div class="header pt-10">October 1, 2019</div>
            </div>
          </div>
        </div>
        <div class="column">
          <div class="ui card">
            <div class="content">
              <div class="description">
                End Date
                <a class="right floated">Change</a>
              </div>
              <div class="header pt-10">April 1, 2020</div>
            </div>
          </div>
        </div>
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

<script>
export default {};
</script>