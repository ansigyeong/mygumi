(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-54a28ab9"],{1428:function(t,e,a){t.exports=a.p+"img/flag.7425da5a.png"},"1dd4":function(t,e,a){"use strict";var n=a("e623"),s=a.n(n);s.a},4385:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("section",{staticClass:"main-container"},[n("AppHeader"),t.isLogin?n("div",{staticClass:"main-history"},[n("p",{staticClass:"main-history__text"},[t._v(t._s(t.username)+"! 어디까지 가봤니?")]),n("div",{staticClass:"main-history__imgbox"},[n("img",{staticClass:"main-history__img",attrs:{src:a("a9d5"),alt:"map"}}),t.mapData.진평동?n("img",{staticClass:"flag flag-jinpeong",attrs:{src:a("1428"),alt:"flag"}}):t._e(),t.mapData.선산읍?n("img",{staticClass:"flag flag-seonsan",attrs:{src:a("1428"),alt:"flag"}}):t._e(),t.mapData.인동?n("img",{staticClass:"flag flag-in",attrs:{src:a("1428"),alt:"flag"}}):t._e()])]):t._e(),n("div",{staticClass:"main-box"},[n("p",{staticClass:"main-box__text"},[t._v("오늘은 어디로 가볼까?")]),n("div",{staticClass:"main-box__fakeInput",on:{click:t.goToSearchPage}},[n("i",{staticClass:"icon ion-md-search"}),n("p",{staticClass:"placeholder"},[t._v("검색")])])]),n("section",{staticClass:"recommend-box"},[n("p",{staticClass:"recommend-title"},[t._v(" 여기는 어때? ")]),n("section",{staticClass:"recommend-card"},[n("img",{staticClass:"recommend-img",attrs:{src:a("692a"),alt:"recommendImg"},on:{click:function(e){return t.goToCoursePage(1)}}})]),n("section",{staticClass:"recommend-card"},[n("img",{staticClass:"recommend-img",attrs:{src:a("484c"),alt:"recommendImg"},on:{click:function(e){return t.goToCoursePage(2)}}})])])],1)},s=[],r=(a("4160"),a("159b"),a("96cf"),a("1da1")),c=a("5530"),i=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},o=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("header",{staticClass:"header-box"},[n("img",{staticClass:"header-img",attrs:{src:a("9d64"),alt:"logo"}})])}],u={},m=u,l=(a("6aa0"),a("2877")),f=Object(l["a"])(m,i,o,!1,null,"47d141b6",null),g=f.exports,d=a("2f62"),p=a("7f87"),h={data:function(){return{username:null,mapData:{"진평동":!1,"인동":!1,"선산읍":!1}}},components:{AppHeader:g},computed:Object(c["a"])(Object(c["a"])({},Object(d["b"])(["isLogined"])),{},{isLogin:function(){return this.isLogined}}),created:function(){this.fetchData(),this.fetchMap()},methods:{fetchData:function(){var t=this;return Object(r["a"])(regeneratorRuntime.mark((function e(){var a,n,s;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return a=t.$store.getters.getId,e.next=3,Object(p["a"])(a);case 3:n=e.sent,s=n.data,t.username=s.user.nickname;case 6:case"end":return e.stop()}}),e)})))()},fetchMap:function(){var t=this;return Object(r["a"])(regeneratorRuntime.mark((function e(){var a,n,s;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return a=t.$store.getters.getId,e.next=3,Object(p["c"])(a);case 3:n=e.sent,s=n.data,s.visited.forEach((function(e){var a=e.place;t.mapData["".concat(a)]=!0}));case 6:case"end":return e.stop()}}),e)})))()},goToSearchPage:function(){this.$router.push("/search")},goToCoursePage:function(t){this.$router.push("/course/".concat(t))}}},_=h,b=(a("1dd4"),Object(l["a"])(_,n,s,!1,null,"a97e3ef0",null));e["default"]=b.exports},"484c":function(t,e,a){t.exports=a.p+"img/course2.2243b88f.png"},"692a":function(t,e,a){t.exports=a.p+"img/course1.8f1c6d8a.png"},"6aa0":function(t,e,a){"use strict";var n=a("ae77"),s=a.n(n);s.a},"7f87":function(t,e,a){"use strict";a.d(e,"a",(function(){return s})),a.d(e,"d",(function(){return r})),a.d(e,"b",(function(){return i})),a.d(e,"c",(function(){return c}));var n=a("365c");function s(t){return n["a"].get("user/".concat(t,"/"))}function r(t,e){return n["a"].patch("user/".concat(t,"/"),e)}function c(t){return n["a"].get("user/".concat(t,"/visited/"))}function i(){return n["a"].get("user/users/")}},"9d64":function(t,e,a){t.exports=a.p+"img/logo.26f15e73.png"},a9d5:function(t,e,a){t.exports=a.p+"img/gumi_map.f19b7ea4.png"},ae77:function(t,e,a){},e623:function(t,e,a){}}]);
//# sourceMappingURL=chunk-54a28ab9.f278a122.js.map