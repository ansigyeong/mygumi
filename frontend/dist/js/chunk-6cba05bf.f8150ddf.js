(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6cba05bf"],{1703:function(t,e,i){"use strict";var o=i("3620"),n=i.n(o);n.a},3620:function(t,e,i){},"833f":function(t,e,i){"use strict";i.r(e);var o=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-app",[i("v-card",{attrs:{tile:""}},[i("div",{staticClass:"card-header"},[i("p",{staticClass:"title"},[t._v("업적")]),i("p",{staticClass:"result"},[t._v(" 🏆 "+t._s(t.completeList.length)+"/"+t._s(t.completeList+t.toDoList.length)+" ")]),i("hr")]),i("v-list",{attrs:{rounded:""}},[i("v-list-item-group",{attrs:{color:"primary"},model:{value:t.selectedItem,callback:function(e){t.selectedItem=e},expression:"selectedItem"}},[i("v-subheader",[t._v("완료한 업적")]),t._l(t.completeList,(function(e,o){return i("v-list-item",{key:o},[i("v-list-item-icon",[i("v-icon",{domProps:{textContent:t._s(e.icon)}})],1),i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(e.text)}}),i("v-list-item-title",{domProps:{textContent:t._s(e.detail)}})],1)],1)})),i("hr"),i("v-subheader",[t._v("잠겨있는 업적")]),t._l(t.toDoList,(function(e,o){return i("v-list-item",{key:o},[i("v-list-item-icon",[i("v-icon",{domProps:{textContent:t._s(e.icon)}})],1),i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(e.text)}}),i("v-list-item-title",{domProps:{textContent:t._s(e.detail)}})],1)],1)}))],2)],1)],1)],1)},n=[],s=(i("96cf"),i("1da1")),c=i("365c");function l(t){return c["b"].get("achievements/".concat(t))}var a={data:function(){return{selectedItem:0,toDoList:[{text:"진평동 마스터",detail:"진평동 미션 10개 완료하기",icon:"mdi-lock",jinpyeong:!1},{text:"금오산 정복자",detail:"금오산 정상에 오르기",icon:"mdi-lock",geumosan:!1},{text:"달려라 자전거",detail:"구미 자전거 종주길 완주",icon:"mdi-lock",bicycle:!1},{text:"서원 러버",detail:"서원 코스 챌린지 완료하기",icon:"mdi-lock",seowon:!1},{text:"구미 탐험가",detail:"랜덤 미션 5개 완료하기",icon:"mdi-lock",explorer:!1},{text:"참된 한국인",detail:"역사 미션 10개 완료하기",icon:"mdi-lock",korean:!1}],completeList:[]}},mounted:function(){this.fetchData()},methods:{fetchData:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var i,o,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,i=t.$store.getters.getId,e.next=4,l(i);case 4:o=e.sent,n=o.data,t.jinpyeong=n.jinpyeong,t.geumosan=n.geumosan,t.bicycle=n.bicycle,t.seowon=n.seowon,t.explorer=n.explorer,t.korean=n.korean,!0===t.jinpyeong&&(t.toDoList.shift(),t.completeList.unshift({text:"진평동 마스터",detail:"진평동에서 미션 10개 완료하기",icon:"mdi-medal",jinpyeong:!0})),!0===t.geumosan&&(t.toDoList.shift(),t.completeList.unshift({text:"금오산 정복자",detail:"금오산 정상에 오르기",icon:"mdi-medal",geumosan:!0})),!0===t.bicycle&&(t.toDoList.shift(),t.completeList.unshift({text:"달려라 자전거",detail:"구미 자전거 종주길 완주",icon:"mdi-medal",bicycle:!0})),!0===t.seowon&&(t.toDoList.shift(),t.completeList.unshift({text:"서원 러버",detail:"서원 코스 챌린지 완료하기",icon:"mdi-medal",seowon:!0})),!0===t.explorer&&(t.toDoList.shift(),t.completeList.unshift({text:"구미 탐험가",detail:"랜덤 미션 5개 완료하기",icon:"mdi-medal",explorer:!0})),!0===t.korean&&(t.toDoList.shift(),t.completeList.unshift({text:"참된 한국인",detail:"역사 미션 10개 완료하기",icon:"mdi-medal",korean:!0})),e.next=23;break;case 20:e.prev=20,e.t0=e["catch"](0),console.log(e.t0);case 23:case"end":return e.stop()}}),e,null,[[0,20]])})))()}}},r=a,m=(i("1703"),i("2877")),d=Object(m["a"])(r,o,n,!1,null,"a8b373b4",null);e["default"]=d.exports}}]);
//# sourceMappingURL=chunk-6cba05bf.f8150ddf.js.map