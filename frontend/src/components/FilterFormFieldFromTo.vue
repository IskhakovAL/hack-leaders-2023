<template>
    <div class="field-from-to">
        <div class="field-from-to__title">{{title}}</div>
        <input class="field-from-to__field" style="width: 50%; height: 24px;" type="number" placeholder="От">
        <input class="field-from-to__field" style="width: 50%; height: 24px;" type="number" placeholder="До">
    </div>
</template>

<script>
export default {
    props: {
        title: String
    }
}
</script>