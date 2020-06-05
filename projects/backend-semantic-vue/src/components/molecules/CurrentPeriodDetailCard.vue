<template>
    <div class="column">
        <div class="ui card">
        <div class="content">
            <div class="description">
            {{ detail_name }}
            <a class="right floated">Change</a>
            </div>
            <div class="header pt-10">{{ detail_value }}</div>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['detail_name', 'detail_value']
}
</script>