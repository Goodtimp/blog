/* jshint esversion: 6 */

function IsMobile () {
  var ua = navigator.userAgent;
  var ipad = ua.match(/(iPad).*OS\s([\d_]+)/);
  var isIphone = !ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/);
  var isAndroid = ua.match(/(Android)\s+([\d.]+)/);
  var isMobile = isIphone || isAndroid;
  // 判断
  return isMobile;
}
/** 判断是否为网址的正则 */
function IsURL (url) {
  var strRegex = "^((https|http|ftp|rtsp|mms)?://)" +
  "?(([0-9a-z_!~*'().&=+$%-]+: )?[0-9a-z_!~*'().&=+$%-]+@)?" + // ftp的user@
   "(([0-9]{1,3}\.){3}[0-9]{1,3}" + // IP形式的URL- 199.194.52.184
   "|" + // 允许IP和DOMAIN（域名）
   "([0-9a-z_!~*'()-]+\.)*" + // 域名- www.
   "([0-9a-z][0-9a-z-]{0,61})?[0-9a-z]\." + // 二级域名
   "[a-z]{2,6})" + // first level domain- .com or .museum
   "(:[0-9]{1,4})?" + // 端口- :80
   "((/?)|" + // a slash isn't required if there is no file name
   "(/[0-9a-z_!~*'().;?:@&=+$,%#-]+)+/?)$";
  var re = new RegExp(strRegex);
  // re.test()
  if (re.test(url)) {
    return (true);
  } else {
    return (false);
  }
}
export default {
  IsMobile,
  IsURL
};
