<template>
  <div>
    <hr />
    <!-- 评论 -->
    <el-row>
      <el-col
        v-for="Comment in comments"
        :key="Comment.Id"
        :span="20"
        :offset="2"
        class="my-comment"
      >
        <div calss="comment-header">
          <a
            :href="Comment.PersonalBlog"
            style="font-size: 1.1em;"
          >
            <img :src="Comment.UserHeader" />
            {{Comment.UserName}}</a>
          <i style="font-size: 0.8em;">发表于：{{Comment.PostedTime}}</i>
        </div>
        <div class="comment-body">
          {{Comment.Content}}
        </div>
      </el-col>
    </el-row>
    <el-row>

      <el-button
        type="primary"
        id="addComment"
        icon="el-icon-edit"
        @click="dialogFormVisible = true"
        circle
      ></el-button>
    </el-row>
    <hr />

    <!-- 发表评论 -->
    <el-dialog
      title="评论"
      :visible.sync="dialogFormVisible"
      @opened="changeForm"
    >
      <el-form
        :model="ruleForm"
        :rules="rules"
        ref="ruleForm"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item
          class="my-line"
          label="评论内容"
          :label-width="formLabelWidth"
          prop="Content"
        >
          <el-input
            type="textarea"
            v-model="ruleForm.Content"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item
          class="my-line"
          label="你的名字"
          :label-width="formLabelWidth"
          prop="UserName"
        >
          <el-input
            v-model="ruleForm.UserName"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item
          class="my-line"
          label="你的主页"
          :label-width="formLabelWidth"
          prop="PersonalBlog"
        >
          <el-input
            v-model="ruleForm.PersonalBlog"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item
          class="my-line"
          label="你的Email"
          :label-width="formLabelWidth"
          prop="UserEmail"
        >
          <el-input
            v-model="ruleForm.UserEmail"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item
          class="my-line"
          label="头像图片"
          :label-width="formLabelWidth"
        >

          <el-select
            v-model="ruleForm.UserHeader"
            style="width: 100%;"
          >
            <el-option
              v-for="header in HeaderPaths"
              :key="header.name"
              :label="header.name"
              :value="header.path"
            ></el-option>
          </el-select>

        </el-form-item>
        <img
          id="HeaderImage"
          src=""
          style="width:20%"
        />
      </el-form>

      <div
        slot="footer"
        class="dialog-footer"
      >
        <el-button
          type="primary"
          @click="submitForm('ruleForm')"
        >评 论</el-button>

        <el-button @click="dialogFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>

  </div>
</template>
<script>
import comment from "../../assets/common.js"
import api from "../../assets/api.js"
export default {
  data() {
    return {
      myWidth: (document.body.clientWidth),
      limitwidth: 600,
      id: this.$route.params.id,
      comments: [],
      HeaderPaths: api.HeaderPath,
      dialogFormVisible: false,
      ruleForm: {
        PersonalBlog: '帮助推广',
        UserName: '善良的陌生小动物',
        UserEmail: '不会泄露你的Email信息',
        UserHeader: '请选择头像'
      },
      rules: {
        Content: [
          { required: true, message: '请输入评论名称', trigger: 'blur' },
          { min: 1, max: 1000, message: '长度在 1 到 1000 个字符', trigger: 'blur' }
        ]    },
      formLabelWidth: '120px'
    }
  },
  methods: {
    GetAllComments() {
      api.GetAllComment(this.id).then(res => {
        this.comments = res;
      });
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.ruleForm.ArticleId = this.id;
          if (this.ruleForm.UserHeader == "请选择头像") {
            this.ruleForm.UserHeader = "null";
          }
          if (this.ruleForm.PersonalBlog.indexOf("http") == -1) {
             this.ruleForm.PersonalBlog = "http://" + this.ruleForm.PersonalBlog;
           }
          if(!comment.IsURL(this.ruleForm.PersonalBlog))
          {
            this.ruleForm.PersonalBlog="#";
          }
          if (this.ruleForm.UserEmail == "不会泄露你的Email信息") {
            this.ruleForm.UserEmail = "hello@e.email";
          }
          //上为数据处理部分
          api.AddComment(this.ruleForm).then(res => {
              this.GetAllComments();
          });
          this.dialogFormVisible = false;
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    changeForm() {
      if (this.limitwidth > this.myWidth) {
        $(".my-line").find("label").css("width", "").next().css("margin-left", "0");
      }
    }
  },
  mounted() {
    this.GetAllComments()
  },
  watch: {
    ruleForm: {
      handler(val, oldValue) {
        if (val.UserHeader != "请选择头像") {
          $("#HeaderImage").attr("src", val.UserHeader);
        }
      },
      deep: true
    },
  },
}
</script>
<style>
.my-comment {
  margin-top: 20px;
  text-align: left;
}
.my-comment img {
  margin-right: 5px;
  width: 50px;
  height: 50px;
  vertical-align: middle;
  border-radius: 50%;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
}
.comment-body {
  margin-left: 10px;
  padding: 0px 0 10px 50px;
}
#addComment {
  border-color: #999;
  background-color: white;
}
#addComment i {
  color: #999;
}

#addComment:hover i {
  color: black;
}
#addComment:hover {
  border-color: black;
}
</style>
