/* jshint esversion: 6 */

import Axios from 'axios';
const RequestApi = "http://47.107.80.19:80/api/";
const Root = "http://47.107.80.19:80/";

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
function postToApi (url) {
  Axios.post(url).then(res => {
    return res;
  }).catch(res => {
    return res;
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

// 得到分类信息通过id
function getCategoryById (id) {
  let url = getRequestUrl("cid?id=" + id);
  return new Promise((resolve, reject) => {
    getToApi(url).then(res => {
      let data = getResponceData(res);
      data.category[0].fields.Id = data.category[0].pk;
      resolve(data.category[0].fields);
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
        let con = data.Content[0].fields;
        con.ContentId = data.Content[0].pk;
        let art = data.Article[0].fields;
        art.Id = data.Article[0].pk;
        data = Object.assign(art, con);
      } catch (err) {
        data = null;
      }
      resolve(data);
    });
  });
}

export default {
  getRequestUrl,
  getAllCategory,
  getCategoryById,
  getToApi,
  getArticleContentById,
  getSameArticleByCId
};
