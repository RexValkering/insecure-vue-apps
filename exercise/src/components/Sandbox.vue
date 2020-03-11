<template>
  <section>
    <h3>Try out your code</h3>
    <hr />

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <label class="font-weight-bold" for="input-vhtml">Input field with v-html binding</label>
          <textarea v-model="firstInput" class="form-control" id="input-vhtml" rows="3"></textarea>
        </div>
        <button class="btn btn-primary" @click="firstInputResult = firstInput">Save</button>
      </div>
      <div class="col-6">
        <label class="font-weight-bold">Rendered result:</label>
        <p v-html="firstInputResult"></p>
      </div>
    </div>

    <hr />

    <div class="row mt-5">
      <div class="col-6">
        <div class="form-group">
          <label class="font-weight-bold" for="input-url">Input field with v-href binding</label>
          <input v-model="secondInput" class="form-control" id="input-url" />
        </div>
      
        <button class="btn btn-primary" @click="secondInputResult = secondInput">Save</button>
      </div>
      <div class="col-6">
    <label class="font-weight-bold">Rendered result:</label>
    <p><a :style="thirdInputResult" :href="secondInputResult">Click me</a></p>
    </div>
    </div>
    <hr />

    <div class="row mt-5">
    <div class="col-6">
    <div class="form-group">
      <label class="font-weight-bold" for="input-style">Input field for styling the above link</label>
      <textarea v-model="thirdInput" class="form-control" id="input-style" rows="3"></textarea>
    </div>
    <button class="btn btn-primary" @click="thirdInputResult = thirdInput">Save</button>
    </div><div class="col-6">
      See link above for result.
    </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      firstInput: "<strong>My input</strong>",
      secondInput: "https://github.com/RexValkering",
      thirdInput: "text-decoration: underline",
      firstInputResult: "<strong>My input</strong>",
      secondInputResult: "https://github.com/RexValkering",
      thirdInputResult: "text-decoration: underline"
    };
  }
};
</script>

<style scoped>
.custom-label {
  position: relative;
}
</style>
