(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-acfda176"],{"293f":function(t,e,n){"use strict";var a=n("6539"),c=n.n(a);c.a},"32f0":function(t,e,n){"use strict";n.d(e,"h",(function(){return c})),n.d(e,"c",(function(){return r})),n.d(e,"b",(function(){return s})),n.d(e,"a",(function(){return u})),n.d(e,"g",(function(){return i})),n.d(e,"i",(function(){return o})),n.d(e,"e",(function(){return l})),n.d(e,"f",(function(){return d})),n.d(e,"d",(function(){return f}));n("99af");var a=n("365c");function c(t){return a["a"].get("schedule/".concat(t,"/"))}function r(t,e){return a["a"].post("schedule/".concat(t,"/"),e)}function s(t,e){return a["a"].post("schedule/".concat(t,"/place/"),e)}function u(t,e){return a["a"].post("schedule/".concat(t,"/invite/"),e)}function i(t,e){return a["a"].get("schedule/".concat(t,"/").concat(e,"/"))}function o(t,e,n){return a["a"].patch("schedule/".concat(t,"/").concat(e,"/"),n)}function l(t,e){return a["a"].delete("schedule/".concat(t,"/").concat(e,"/place/"))}function d(t,e){return a["a"].delete("schedule/".concat(t,"/").concat(e,"/"))}function f(t,e){return a["a"].delete("schedule/".concat(t,"/").concat(e,"/invite/"))}},"54dd":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-app",[n("div",{staticClass:"plan-wrapper"},[n("header",{staticClass:"header"},[n("div",{staticClass:"container"},[n("span",[t._v(t._s(t.scheduleTitle))]),n("v-btn",{staticStyle:{position:"absolute",right:"0px"},attrs:{small:"",text:"",color:"primary"},on:{click:t.goToPlanUpdatePage}},[t._v("수정 "),n("v-icon",[t._v("mdi-pencil-box-outline")])],1)],1)]),n("section",{staticClass:"today-box",attrs:{id:"today-box"}},[n("span",{staticClass:"breadcrumb"},[t._v("여행 날짜")]),n("p",{staticStyle:{"font-size":"20px",padding:"16px 40px 0px"}},[t._v(" "+t._s(t.viewDate)+" ")])]),n("section",{staticClass:"upcoming-events"},[n("div",{staticClass:"container"},[n("h3",{staticStyle:{"margin-bottom":"20px"}},[t._v(" 여행 일정 ")]),n("div",{staticClass:"events-wrapper"},[t._l(t.plans,(function(e){return n("div",{key:e.id,staticClass:"event"},[n("h4",{staticClass:"event__point"},[t._v(t._s(e.place))]),n("p",{staticClass:"event__description"},[t._v(" "+t._s(e.dong)+" ")])])})),n("v-row",{staticClass:"event active"},[n("i",{staticClass:"ion ion-ios-radio-button-on icon-in-active-mode"}),n("div",{staticStyle:{width:"70%"}},[n("span",{staticClass:"event__point"},[t._v("함께 갈 친구")]),n("br"),t._l(t.friends,(function(e,a){return n("span",{key:a,staticClass:"event__description"},[t._v(" "+t._s(e)+" ")])}))],2),n("v-spacer")],1)],2),n("v-btn",{staticClass:"add-event-button",attrs:{text:""},on:{click:t.goToChallengePage}},[n("span",{staticClass:"add-event-button__title"},[t._v("여행 시작")]),n("span",{staticClass:"add-event-button__icon"},[n("v-icon",[t._v("mdi-playlist-plus")])],1)])],1)])])])},c=[],r=(n("96cf"),n("1da1")),s=n("32f0"),u=n("674f"),i={data:function(){return{selectDate:(new Date).toISOString().substr(0,10),viewDate:null,friends:[],userId:null,scheduleId:null,scheduleData:[],scheduleTitle:null,placeData:[],plans:[]}},mounted:function(){this.userId=this.$store.getters.getId,this.scheduleId=this.$route.params.scheduleId,this.fetchSchedule()},methods:{fetchSchedule:function(){var t=this;return Object(r["a"])(regeneratorRuntime.mark((function e(){var n,a,c,r,u,i,o;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,Object(s["g"])(t.userId,t.scheduleId);case 3:for(n=e.sent,a=n.data,t.scheduleData=a.data[0],t.placeData=t.scheduleData.place,t.selectDate=t.scheduleData.date,t.scheduleTitle=t.scheduleData.title,c=t.selectDate[5]+t.selectDate[6],r=t.selectDate[9],t.selectDate[8]&&(r=t.selectDate[8]+t.selectDate[9]),u=t.selectDate[0]+t.selectDate[1]+t.selectDate[2]+t.selectDate[3],t.viewDate=c+"월 "+r+"일, "+u+"년",i=0;i<=t.placeData.length-1;i++)t.fetchPlace(t.placeData[i]);for(o=0;o<=t.scheduleData.user.length-1;o++)t.friends.push(t.scheduleData.user[o].nickname);e.next=21;break;case 18:e.prev=18,e.t0=e["catch"](0),console.log(e.t0);case 21:case"end":return e.stop()}}),e,null,[[0,18]])})))()},fetchPlace:function(t){var e=this;return Object(r["a"])(regeneratorRuntime.mark((function n(){var a,c;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.prev=0,n.next=3,Object(u["f"])(t);case 3:a=n.sent,c=a.data,e.plans.push(c.data),n.next=11;break;case 8:n.prev=8,n.t0=n["catch"](0),console.log(n.t0);case 11:case"end":return n.stop()}}),n,null,[[0,8]])})))()},goToPlanUpdatePage:function(){return this.$router.push("/plan/".concat(this.scheduleId,"/update"))},goToChallengePage:function(){return this.$router.push("/challenge/".concat(this.scheduleId))}}},o=i,l=(n("293f"),n("2877")),d=Object(l["a"])(o,a,c,!1,null,"e8cba1b2",null);e["default"]=d.exports},6539:function(t,e,n){},"674f":function(t,e,n){"use strict";n.d(e,"f",(function(){return c})),n.d(e,"a",(function(){return r})),n.d(e,"d",(function(){return s})),n.d(e,"e",(function(){return u})),n.d(e,"b",(function(){return i})),n.d(e,"c",(function(){return o}));n("99af");var a=n("365c");function c(t){return a["b"].get("tour/place/".concat(t,"/"))}function r(t){return a["b"].get("tour/".concat(t,"/"))}function s(t){return a["a"].get("tour/search/".concat(t,"/"))}function u(t,e){return a["a"].get("tour/search/".concat(t,"/").concat(e,"/"))}function i(t,e){return a["a"].delete("tour/search/".concat(t,"/").concat(e,"/"))}function o(t){return a["a"].get("territory/".concat(t))}},"99af":function(t,e,n){"use strict";var a=n("23e7"),c=n("d039"),r=n("e8b5"),s=n("861d"),u=n("7b0b"),i=n("50c4"),o=n("8418"),l=n("65f0"),d=n("1dde"),f=n("b622"),h=n("2d00"),p=f("isConcatSpreadable"),v=9007199254740991,g="Maximum allowed index exceeded",b=h>=51||!c((function(){var t=[];return t[p]=!1,t.concat()[0]!==t})),_=d("concat"),D=function(t){if(!s(t))return!1;var e=t[p];return void 0!==e?!!e:r(t)},w=!b||!_;a({target:"Array",proto:!0,forced:w},{concat:function(t){var e,n,a,c,r,s=u(this),d=l(s,0),f=0;for(e=-1,a=arguments.length;e<a;e++)if(r=-1===e?s:arguments[e],D(r)){if(c=i(r.length),f+c>v)throw TypeError(g);for(n=0;n<c;n++,f++)n in r&&o(d,f,r[n])}else{if(f>=v)throw TypeError(g);o(d,f++,r)}return d.length=f,d}})}}]);
//# sourceMappingURL=chunk-acfda176.f7984a9a.js.map