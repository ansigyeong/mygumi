(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a5ab5266"],{1428:function(t,a,e){t.exports=e.p+"img/flag.7425da5a.png"},"3fd8":function(t,a,e){"use strict";var n=e("fc5b"),s=e.n(n);s.a},4385:function(t,a,e){"use strict";e.r(a);var n=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("section",{staticClass:"main-container"},[n("AppHeader"),t.isLogin?n("div",{staticClass:"main-history"},[n("p",{staticClass:"main-history__text"},[t._v(t._s(t.username)+"! 어디까지 가봤니?")]),n("div",{staticClass:"main-history__imgbox"},[n("img",{staticClass:"main-history__img",attrs:{src:e("a9d5"),alt:"map"}}),t.mapData.진평동?n("img",{staticClass:"flag flag-jinpeong",attrs:{src:e("1428"),alt:"flag"}}):t._e(),t.mapData.선산읍?n("img",{staticClass:"flag flag-seonsan",attrs:{src:e("1428"),alt:"flag"}}):t._e(),t.mapData.인동?n("img",{staticClass:"flag flag-in",attrs:{src:e("1428"),alt:"flag"}}):t._e()])]):t._e(),n("div",{staticClass:"main-box"},[n("p",{staticClass:"main-box__text"},[t._v("오늘은 어디로 가볼까?")]),n("div",{staticClass:"main-box__fakeInput",on:{click:t.goToSearchPage}},[n("i",{staticClass:"icon ion-md-search"}),n("p",{staticClass:"placeholder"},[t._v("검색")])])]),n("section",{staticClass:"recommend-box"},[n("p",{staticClass:"recommend-title"},[t._v(" 여기는 어때? ")]),n("section",{staticClass:"recommend-card"},[n("img",{staticClass:"recommend-img",attrs:{src:e("692a"),alt:"recommendImg"},on:{click:function(a){return t.goToCoursePage(1)}}})]),n("section",{staticClass:"recommend-card"},[n("img",{staticClass:"recommend-img",attrs:{src:e("484c"),alt:"recommendImg"},on:{click:function(a){return t.goToCoursePage(2)}}})])])],1)},s=[],c=(e("4160"),e("159b"),e("96cf"),e("1da1")),r=e("5530"),i=function(){var t=this,a=t.$createElement;t._self._c;return t._m(0)},o=[function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("header",{staticClass:"header-box"},[n("img",{staticClass:"header-img",attrs:{src:e("9d64"),alt:"logo"}})])}],u={},m=u,f=(e("6aa0"),e("2877")),l=Object(f["a"])(m,i,o,!1,null,"47d141b6",null),g=l.exports,d=e("2f62"),p=e("7f87"),h={data:function(){return{username:null,mapData:{"진평동":!1,"인동":!1,"선산읍":!1}}},components:{AppHeader:g},computed:Object(r["a"])(Object(r["a"])({},Object(d["b"])(["isLogined"])),{},{isLogin:function(){return this.isLogined}}),created:function(){this.isLogined&&(this.fetchData(),this.fetchMap())},methods:{fetchData:function(){var t=this;return Object(c["a"])(regeneratorRuntime.mark((function a(){var e,n,s;return regeneratorRuntime.wrap((function(a){while(1)switch(a.prev=a.next){case 0:return e=t.$store.getters.getId,a.next=3,Object(p["a"])(e);case 3:n=a.sent,s=n.data,t.username=s.user.nickname;case 6:case"end":return a.stop()}}),a)})))()},fetchMap:function(){var t=this;return Object(c["a"])(regeneratorRuntime.mark((function a(){var e,n,s;return regeneratorRuntime.wrap((function(a){while(1)switch(a.prev=a.next){case 0:return e=t.$store.getters.getId,a.next=3,Object(p["c"])(e);case 3:n=a.sent,s=n.data,s.visited.forEach((function(a){var e=a.place;t.mapData["".concat(e)]=!0}));case 6:case"end":return a.stop()}}),a)})))()},goToSearchPage:function(){this.$router.push("/search")},goToCoursePage:function(t){this.$router.push("/course/".concat(t))}}},_=h,b=(e("3fd8"),Object(f["a"])(_,n,s,!1,null,"94ea2708",null));a["default"]=b.exports},"484c":function(t,a,e){t.exports=e.p+"img/course2.2243b88f.png"},"692a":function(t,a,e){t.exports=e.p+"img/course1.8f1c6d8a.png"},"6aa0":function(t,a,e){"use strict";var n=e("ae77"),s=e.n(n);s.a},"7f87":function(t,a,e){"use strict";e.d(a,"a",(function(){return s})),e.d(a,"d",(function(){return c})),e.d(a,"b",(function(){return i})),e.d(a,"c",(function(){return r}));var n=e("365c");function s(t){return n["a"].get("user/".concat(t,"/"))}function c(t,a){return n["a"].patch("user/".concat(t,"/"),a)}function r(t){return n["a"].get("user/".concat(t,"/visited/"))}function i(){return n["a"].get("user/users/")}},"9d64":function(t,a,e){t.exports=e.p+"img/logo.26f15e73.png"},a9d5:function(t,a,e){t.exports=e.p+"img/gumi_map.f19b7ea4.png"},ae77:function(t,a,e){},fc5b:function(t,a,e){}}]);
//# sourceMappingURL=chunk-a5ab5266.58ef80bb.js.map