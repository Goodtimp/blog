webpackJsonp([3],{"6gVp":function(t,e,a){"use strict";var n={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"my-toolheader"},[e("h1",[this._v("\n      "+this._s(this.ToolName)+" \n    "),e("br"),this._v(" "),e("small",{staticStyle:{"font-size":"0.5em"}},[this._v(this._s(this.introduction))])])])},staticRenderFns:[]};var r=a("VU/8")({data:function(){return{}},props:["ToolName","introduction"]},n,!1,function(t){a("7trK")},null,null);e.a=r.exports},"7trK":function(t,e){},HJH0:function(t,e,a){"use strict";var n={data:function(){return{UploadFileUrl:this.api.UploadFileUrl,imageUrl:""}},methods:{handleAvatarSuccess:function(t,e){this.imageUrl=URL.createObjectURL(e.raw),this.$emit("child-msg",this.imageUrl)},beforeAvatarUpload:function(t){var e="image/jpeg"===t.type||"image/png"===t.type,a=t.size/1024/1024<10;return e||this.$message.error("上传头像图片只能是 JPG 格式!"),a||this.$message.error("上传头像图片大小不能超过 10MB!"),e&&a}}},r={render:function(){var t=this.$createElement,e=this._self._c||t;return e("el-upload",{staticClass:"avatar-uploader",attrs:{action:this.UploadFileUrl,"show-file-list":!1,"on-success":this.handleAvatarSuccess,"before-upload":this.beforeAvatarUpload,name:"userfile"}},[this.imageUrl?e("img",{staticClass:"avatar",attrs:{src:this.imageUrl,id:"uploadImage"}}):e("i",{staticClass:"el-icon-plus avatar-uploader-icon"})])},staticRenderFns:[]};var i=a("VU/8")(n,r,!1,function(t){a("mhYo")},null,null);e.a=i.exports},QMVH:function(t,e){},hNcb:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("Iazu"),r=a("6gVp"),i=a("HJH0"),s={data:function(){return{data:[],imagepath:"",form:{url:""}}},methods:{getSpeech:function(){var t=this;""==this.form.url?this.$message({message:"你还没添加链接呢！",type:"warning"}):this.api.GetSpeech({url:this.form.url}).then(function(e){0!=e.return&&(t.common.IsMobile()?window.location.href=t.api.Root+e.url.substr(2):"download"in document.createElement("a")?(alert(e.url),t.api.funDownload(e.content,e.name)):eleButton.onclick=function(){this.$message({message:"浏览器不支持",type:"warning"})})}).catch(function(e){t.$message({message:"错误！",type:"Error"})})}},components:{"v-header":r.a,"v-upload":i.a}},o={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-main",{staticStyle:{"text-align":"center"}},[a("v-header",{attrs:{ToolName:"英语演讲稿",introduction:"从指定网页利用爬虫，下载演讲稿以及翻译信息"}}),t._v(" "),a("div",{staticStyle:{margin:"100px 10% 50px 10%","text-indent":"2em"}},[a("a",{attrs:{href:"http://www.kekenet.com/Article/15539/",target:"_blank"}},[t._v("网页链接")])]),t._v(" "),a("el-form",{attrs:{model:t.form}},[a("el-form-item",{attrs:{label:"链接地址"}},[a("el-input",{attrs:{type:"textarea"},model:{value:t.form.url,callback:function(e){t.$set(t.form,"url",e)},expression:"form.url"}})],1)],1),t._v(" "),a("el-button",{staticStyle:{margin:"20px 0px"},on:{click:t.getSpeech}},[t._v("获取该篇")]),t._v(" "),a("div")],1)},staticRenderFns:[]};var l=a("VU/8")(s,o,!1,function(t){a("QMVH")},null,null).exports,c={data:function(){return{}},components:{"v-aside":n.a,"v-main":l}},u={render:function(){var t=this.$createElement,e=this._self._c||t;return e("el-container",{staticClass:"el-carousel",staticStyle:{height:"100%"}},[e("v-aside"),this._v(" "),e("v-main")],1)},staticRenderFns:[]};var m=a("VU/8")(c,u,!1,function(t){a("wiq0")},null,null);e.default=m.exports},mhYo:function(t,e){},wiq0:function(t,e){}});
//# sourceMappingURL=3.293e94792d57c26b71c7.js.map