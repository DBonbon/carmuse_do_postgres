!function(){"use strict";var e,t={83622:function(e,t,r){var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var o=n(r(73609));o.default((function(){o.default("button.action-set-privacy").on("click",(function(){return ModalWorkflow({url:this.getAttribute("data-url"),onload:{set_privacy:function(e){o.default("form",e.body).on("submit",(function(){return e.postForm(this.action,o.default(this).serialize()),!1}));var t=o.default("input[name='restriction_type'][value='password']",e.body),r=o.default("input[name='restriction_type'][value='groups']",e.body),n=o.default(".password-field",e.body),i=o.default("#groups-fields",e.body);function a(){t.is(":checked")?(n.show(),i.hide()):r.is(":checked")?(n.hide(),i.show()):(n.hide(),i.hide())}a(),o.default("input[name='restriction_type']",e.body).on("change",a)},set_privacy_done:function(e,t){e.respond("setPermission",t.is_public),e.close()}},responses:{setPermission:function(e){e?(o.default(".privacy-indicator").removeClass("private").addClass("public"),o.default(".privacy-indicator-tag").addClass("u-hidden").attr("aria-hidden","true")):(o.default(".privacy-indicator").removeClass("public").addClass("private"),o.default(".privacy-indicator-tag").removeClass("u-hidden").attr("aria-hidden","false"))}}}),!1}))}))},73609:function(e){e.exports=jQuery}},r={};function n(e){var o=r[e];if(void 0!==o)return o.exports;var i=r[e]={id:e,loaded:!1,exports:{}};return t[e].call(i.exports,i,i.exports,n),i.loaded=!0,i.exports}n.m=t,e=[],n.O=function(t,r,o,i){if(!r){var a=1/0;for(s=0;s<e.length;s++){r=e[s][0],o=e[s][1],i=e[s][2];for(var u=!0,d=0;d<r.length;d++)(!1&i||a>=i)&&Object.keys(n.O).every((function(e){return n.O[e](r[d])}))?r.splice(d--,1):(u=!1,i<a&&(a=i));u&&(e.splice(s--,1),t=o())}return t}i=i||0;for(var s=e.length;s>0&&e[s-1][2]>i;s--)e[s]=e[s-1];e[s]=[r,o,i]},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,{a:t}),t},n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},n.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),n.hmd=function(e){return(e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.j=598,function(){var e={598:0};n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,i,a=r[0],u=r[1],d=r[2],s=0;for(o in u)n.o(u,o)&&(n.m[o]=u[o]);if(d)var c=d(n);for(t&&t(r);s<a.length;s++)i=a[s],n.o(e,i)&&e[i]&&e[i][0](),e[a[s]]=0;return n.O(c)},r=self.webpackChunkwagtail=self.webpackChunkwagtail||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}(),n.O(void 0,[751],(function(){return n(83622)}));var o=n.O(void 0,[751],(function(){return n(90971)}));o=n.O(o)}();
//# sourceMappingURL=privacy-switch.js.map