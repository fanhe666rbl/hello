<template>
  <div class="home">
    <h1>{{this.testData}}</h1>
    <el-button @click="getData('aaa')">拿数据</el-button>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data(){
    return{
      testData:'aaa'
    }
  },
  methods:{
    getData(name) {
      alert(name)
      this.$axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/test/',
        data: {
          name: name,
        }
      }).then((res) => {
        alert(res.data);
        // this.testData = res.data.num

      });
      // alert(name)
    },
  }
}
</script>