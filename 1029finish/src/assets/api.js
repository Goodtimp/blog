/* jshint esversion: 6 */

import Axios from 'axios';
var qs = require('qs');
const Root = "http://47.107.80.19/";
const RequestApi = Root + "api/";
const UploadRoot = "/static/upload/";
const UploadFileUrl = RequestApi + "upload/";
const GetSpeechUrl = RequestApi + "pyrequest/";
const HeaderPath = [
  { name: "rabbit", path: "/static/images/CommentHeader/rabbit.jpg" },
  { name: "bear", path: "/static/images/CommentHeader/bear.jpg" },
  { name: "smile", path: "/static/images/CommentHeader/smile.jpg" },
  { name: "girl", path: "/static/images/CommentHeader/girl.jpg" },
  { name: "rhizomys", path: "/static/images/CommentHeader/rhizomys.jpg" },
  { name: "duck", path: "/static/images/CommentHeader/duck.jpg" },
  {name: "xiaohuangren", path: "/static/images/CommentHeader/xiaohuangren.jpg"}
];

// 获取请求连接
function getRequestUrl (str) {
  let url = RequestApi + str;
  return url;
}

// 以get方法请求api
function getToApi (url) {
  return Axios.get(url);
}

// 以pos方法请求api
function postToApi (url, data) {
  return Axios.post(url, qs.stringify(data), {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
  });
}

// 得到响应数据主体
function getResponceData (res) {
  try {
    return res.data;
  } catch (err) {
    return res;
  }
}
// 修改图片地址，应对上传图片无Upload_Root
function changeImagePath (image) {
  if (image.indexOf("static") === -1) {
    image = UploadRoot + image;
  }
  return image;
}

// 修改时间格式
function changeTimeFormat (time) {
  if (time.indexOf("T") > -1) {
    time = time.replace("T", " ");
  }
  if (time.indexOf(".") > 0) {
    time = time.substr(0, 19);
  }
  return time;
}

// 得到所有的分类信息
function getAllCategory () {
  let data;

  let url = getRequestUrl("cid?id=0");
  let list = [];
  return new Promise((resolve, reject) => {
    getToApi(url).then(res => {
      data = getResponceData(res);
      for (var i = 0; i < data.category.length; i++) {
        let line = data.category[i].fields;
        line.Id = data.category[i].pk;
        list.push(line);
      }
      resolve(list);
    });
  });
}

// 通过id得到分类信息
function getCategoryById (id) {
  let url = getRequestUrl("cid?id=" + id);
  return new Promise((resolve, reject) => {
    getToApi(url).then(res => {
      let data = getResponceData(res);
      data.category[0].fields.Id = data.category[0].pk;
      data = data.category[0].fields;
      data.BackgroundPath = changeImagePath(data.BackgroundPath);
      data.CategoryLog = changeImagePath(data.CategoryLog);
      resolve(data);
    });
  });
}

// 得到相同分类的文章概略 通过cid
function getSameArticleByCId (id) {
  let url = getRequestUrl("acid?id=" + id);
  return new Promise((resolve, reject) => {
    getToApi(url).then(res => {
      let data = getResponceData(res);
      let list = [];
      for (var i = 0; i < data.Articles.length; i++) {
        let line = data.Articles[i].fields;
        line.Id = data.Articles[i].pk;
        line.BackgroundPath = changeImagePath(line.BackgroundPath);
        list.push(line);
      }
      resolve(list);
    });
  });
}

// 得到相同分类的文章概略 通过cid
function getSameArticleByCIdPage (id, page) {
  let url = getRequestUrl("acidp");
  return new Promise((resolve, reject) => {
    postToApi(url, {
      id: id,
      page: page
    }).then(res => {
      let data = getResponceData(res);
      let list = [];
      for (var i = 0; i < data.Articles.length; i++) {
        let line = data.Articles[i].fields;
        line.Id = data.Articles[i].pk;
        line.BackgroundPath = changeImagePath(line.BackgroundPath);
        list.push(line);
      }
      resolve(list);
    });
  });
}

// 通过id得到文章概略
function getArticleById (id) {
  let url = getRequestUrl("aid?id=" + id);
  return getResponceData(getToApi(url));
}

// 通过id得到文章内容
function getArticleContentById (id) {
  let url = getRequestUrl("id?id=" + id);
  return new Promise((resolve, reject) => {
    getToApi(url).then(res => {
      let data;
      try {
        data = getResponceData(res);
        let art = data.Article[0].fields; // 获取文章信息
        art.PostedTime = changeTimeFormat(art.PostedTime);
        art.Id = data.Article[0].pk;
        art.LastDataChange = changeTimeFormat(art.LastDataChange);
        // art.like = data.like;
        art.BackgroundPath = changeImagePath(art.BackgroundPath);

        data = Object.assign(art);
      } catch (err) {
        data = null;
      }
      resolve(data);
    });
  });
}

//    getToApi(url).then(res => {

function AddLikeNum (articlid) {
  let url = getRequestUrl("like");
  return new Promise((resolve, reject) => {
    postToApi(url, {
      id: articlid
    }).then(res => {
      resolve(res);
    }).catch(res => {
      resolve(res);
    });
  });
}

/**
 * 添加评论 参数为键值对 包括{Content,ArticleId,UserName,UserEmail,UserHeader}
 * @param {评论} comment
 */
function AddComment (comment) {
  let url = getRequestUrl("comment");
  return new Promise((resolve, reject) => {
    postToApi(url, comment).then(res => {
      resolve(res);
    }).catch(res => {
      resolve(res);
    });
  });
}

/**
 * 获取所有评论信息
 */
function GetAllComment (ArticleId) {
  // 获取文章评论
  let url = getRequestUrl("getallcom");

  return new Promise((resolve, reject) => {
    postToApi(url, { id: ArticleId }).then(res => {
      let data = getResponceData(res);
      let Comments = [];
      for (var i = data.Comments.length - 1; i >= 0; i--) {
        let line = data.Comments[i].fields;
        line.UserHeader = changeImagePath(line.UserHeader);
        line.PostedTime = changeTimeFormat(line.PostedTime);
        line.Id = data.Comments[i].pk;
        Comments.push(line);
      }
      resolve(Comments);
    }).catch(res => {
      resolve(res);
    });
  });
}

/**
 * 某IP是否点赞
 */
function GetArticleLike (ArticleId) {
  let url = getRequestUrl("like");
  return new Promise((resolve, reject) => {
    postToApi(url, { id: ArticleId, is: 1 }).then(res => {
      let data = getResponceData(res);
      resolve(data);
    }).catch(res => {
      resolve(res);
    });
  });
}

/**
 * upload file
 */
function UploadFile (formdata) {
  var options = { // 设置axios的参数
    url: UploadFileUrl,
    data: formdata,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  };
  return Axios(options);
}

/**
 * get speech
 */
function GetSpeech (data) {
  return new Promise((resolve, reject) => {
    data.mode = 1;
    postToApi(GetSpeechUrl, data).then(res => {
      resolve(getResponceData(res));
    }).catch(res => {
      resolve({'return': 0});
    });
  });
}

/** 修改该头信息Content-Disposition 以get请求 */
function funDownload (content, filename) {
  var eleLink = document.createElement('a');
  eleLink.download = filename;
  eleLink.style.display = 'none';
  // 字符内容转变成blob地址
  var blob = new Blob([content]);
  eleLink.href = URL.createObjectURL(blob);
  // 触发点击
  document.body.appendChild(eleLink);
  eleLink.click();
  // 然后移除
  document.body.removeChild(eleLink);
}

export default {
  getRequestUrl,
  getAllCategory,
  getCategoryById,
  getToApi,
  getArticleContentById,
  getSameArticleByCId,
  UploadRoot,
  Root,
  changeImagePath,
  AddLikeNum,
  AddComment,
  HeaderPath,
  GetAllComment,
  GetArticleLike,
  UploadFile,
  UploadFileUrl,
  GetSpeech,
  funDownload,
  getSameArticleByCIdPage
};
