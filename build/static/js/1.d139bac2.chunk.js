(window.webpackJsonp=window.webpackJsonp||[]).push([[1],{1817:function(e,t,a){"use strict";a.r(t);var n=a(7),c=a(8),r=a(13),o=a(12),l=a(14),i=a(0),s=a.n(i),u=a(43),m=a(10),d=a(22),p=a(93),h=a(23),C=a(172),f=a(6),E=a(1),g=a(491),b=a(38),v=a.n(b),O="[CONTACTS APP] GET USER DATA";function N(){var e=v.a.get("/api/contacts-app/user");return function(t){return e.then(function(e){return t({type:O,payload:e.data})})}}var T=a(64),y="[CONTACTS APP] GET CONTACTS",A="[CONTACTS APP] SET SEARCH TEXT",P="[CONTACTS APP] TOGGLE IN SELECTED CONTACTS",S="[CONTACTS APP] SELECT ALL CONTACTS",j="[CONTACTS APP] DESELECT ALL CONTACTS",D="[CONTACTS APP] OPEN NEW CONTACT DIALOG",w="[CONTACTS APP] CLOSE NEW CONTACT DIALOG",I="[CONTACTS APP] OPEN EDIT CONTACT DIALOG",k="[CONTACTS APP] CLOSE EDIT CONTACT DIALOG",x="[CONTACTS APP] ADD CONTACT",L="[CONTACTS APP] UPDATE CONTACT",M="[CONTACTS APP] REMOVE CONTACT",_="[CONTACTS APP] REMOVE CONTACTS",R="[CONTACTS APP] TOGGLE STARRED CONTACT",W="[CONTACTS APP] TOGGLE STARRED CONTACTS",G="[CONTACTS APP] SET CONTACTS STARRED ",U="[CONTACTS APP] OPEN CONFIRM DIALOG",H="[CONTACTS APP] CLOSE CONFIRM DIALOG";function F(e){var t=v.a.get(T.a.baseUrl+"/admin/users/"+e+"/");return function(e){return t.then(function(t){return e({type:y,payload:t.data.friends})})}}function X(e){return{type:P,contactId:e}}function B(){return{type:S}}function q(){return{type:j}}function J(){return{type:D}}function z(){return{type:w}}function Y(e){return{type:I,data:e}}function V(){return{type:k}}function K(e){return{type:U,data:e}}function Q(){return{type:H}}function Z(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/add-contact",{newContact:e}).then(function(e){return Promise.all([t({type:x})]).then(function(){return t(F(n))})})}}function $(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/update-contact",{contact:e}).then(function(e){return Promise.all([t({type:L})]).then(function(){return t(F(n))})})}}function ee(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/remove-contact",{contactId:e}).then(function(e){return Promise.all([t({type:M})]).then(function(){return t(F(n))})})}}function te(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/remove-contacts",{contactIds:e}).then(function(e){return Promise.all([t({type:_}),t({type:j})]).then(function(){return t(F(n))})})}}function ae(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/toggle-starred-contact",{contactId:e}).then(function(e){return Promise.all([t({type:R}),t(N())]).then(function(){return t(F(n))})})}}function ne(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/toggle-starred-contacts",{contactIds:e}).then(function(e){return Promise.all([t({type:W}),t({type:j}),t(N())]).then(function(){return t(F(n))})})}}function ce(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/set-contacts-starred",{contactIds:e}).then(function(e){return Promise.all([t({type:G}),t({type:j}),t(N())]).then(function(){return t(F(n))})})}}function re(e){return function(t,a){var n=a().contactsApp.contacts.routeParams;return v.a.post("/api/contacts-app/set-contacts-unstarred",{contactIds:e}).then(function(e){return Promise.all([t({type:G}),t({type:j}),t(N())]).then(function(){return t(F(n))})})}}var oe=function(e){function t(){var e,a;Object(n.a)(this,t);for(var c=arguments.length,l=new Array(c),i=0;i<c;i++)l[i]=arguments[i];return(a=Object(r.a)(this,(e=Object(o.a)(t)).call.apply(e,[this].concat(l)))).state={selectedContactsMenu:null},a.getFilteredArray=function(e,t){var a=Object.keys(e).map(function(t){return e[t]});return 0===t.length?a:m.t.filterArrayByString(a,t)},a.openSelectedContactMenu=function(e){a.setState({selectedContactsMenu:e.currentTarget})},a.closeSelectedContactsMenu=function(){a.setState({selectedContactsMenu:null})},a}return Object(l.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){var e=this,t=this.props,a=t.contacts,n=t.searchText,c=t.selectedContactIds,r=t.openEditContactDialog,o=t.confirmDialog,l=t.removeContacts,i=t.setContactsUnstarred,u=t.setContactsStarred,d=this.getFilteredArray(a,n),p=this.state.selectedContactsMenu;return d||0!==d.length?s.a.createElement(m.b,{animation:"transition.slideUpIn",delay:300},s.a.createElement(g.b,{className:"-striped -highlight border-0",getTrProps:function(e,t,a){return{className:"cursor-pointer",onClick:function(e,a){t&&r(t.original)}}},data:d,columns:[{Header:"No",accessor:"",Cell:function(e){return e.index+1},width:64,filterable:!1,className:"justify-center"},{Header:function(){return c.length>0&&s.a.createElement(s.a.Fragment,null,s.a.createElement(E.x,{"aria-owns":p?"selectedContactsMenu":null,"aria-haspopup":"true",onClick:e.openSelectedContactMenu},s.a.createElement(E.w,null,"more_horiz")),s.a.createElement(E.H,{id:"selectedContactsMenu",anchorEl:p,open:Boolean(p),onClose:e.closeSelectedContactsMenu},s.a.createElement(E.J,null,s.a.createElement(E.I,{onClick:function(){l(c),e.closeSelectedContactsMenu()}},s.a.createElement(E.E,null,s.a.createElement(E.w,null,"delete")),s.a.createElement(E.F,{inset:!0,primary:"Remove"})),s.a.createElement(E.I,{onClick:function(){u(c),e.closeSelectedContactsMenu()}},s.a.createElement(E.E,null,s.a.createElement(E.w,null,"star")),s.a.createElement(E.F,{inset:!0,primary:"Starred"})),s.a.createElement(E.I,{onClick:function(){i(c),e.closeSelectedContactsMenu()}},s.a.createElement(E.E,null,s.a.createElement(E.w,null,"star_border")),s.a.createElement(E.F,{inset:!0,primary:"Unstarred"})))))},accessor:"picture",Cell:function(e){return s.a.createElement(E.b,{alt:e.original.name,src:e.value})},className:"justify-center",width:64,sortable:!1},{Header:"Name",accessor:"name",filterable:!1},{Header:"User name",accessor:"username",filterable:!1},{Header:"Email",accessor:"email",filterable:!1},{Header:"Email verified",accessor:"email_verified",Cell:function(e){return s.a.createElement("div",null,!0===e.value?"Yes":"No")},filterable:!1},{Header:"Phone Number",accessor:"phone_number",filterable:!1},{Header:"Phone Number verified",accessor:"Phone_number_verified",Cell:function(e){return s.a.createElement("div",null,!0===e.value?"Yes":"No")},filterable:!1},{Header:"Label in use",accessor:"label_in_use",filterable:!1},{Header:"Photo in use",accessor:"photo_in_use",filterable:!1},{Header:"",width:64,className:"justify-center",Cell:function(e){return s.a.createElement("div",{className:"flex items-center"},s.a.createElement(E.x,{onClick:function(t){t.stopPropagation(),o(e.original.id)}},s.a.createElement(E.w,null,"delete")))}}],defaultPageSize:10,noDataText:"No contacts found"})):s.a.createElement("div",{className:"flex items-center justify-center h-full"},s.a.createElement(E.ab,{color:"textSecondary",variant:"h5"},"There are no contacts!"))}}]),t}(i.Component);var le=Object(p.g)(Object(h.b)(function(e){var t=e.friendsApp;return{contacts:t.contacts.entities,selectedContactIds:t.contacts.selectedContactIds,searchText:t.contacts.searchText,user:t.user}},function(e){return Object(d.c)({getContacts:F,getUserData:N,toggleInSelectedContacts:X,selectAllContacts:B,deSelectAllContacts:q,openEditContactDialog:Y,removeContacts:te,toggleStarredContact:ae,toggleStarredContacts:ne,setContactsStarred:ce,setContactsUnstarred:re,confirmDialog:K},e)})(oe)),ie=a(16),se={id:"",name:"",lastName:"",avatar:"assets/images/avatars/profile.jpg",nickname:"",company:"",jobTitle:"",email:"",phone:"",address:"",birthday:"",notes:""},ue=function(e){function t(){var e,a;Object(n.a)(this,t);for(var c=arguments.length,l=new Array(c),i=0;i<c;i++)l[i]=arguments[i];return(a=Object(r.a)(this,(e=Object(o.a)(t)).call.apply(e,[this].concat(l)))).state=Object(ie.a)({},se),a.handleChange=function(e){a.setState(f.a.set(Object(ie.a)({},a.state),e.target.name,"checkbox"===e.target.type?e.target.checked:e.target.value))},a.closeComposeDialog=function(){"edit"===a.props.contactDialog.type?a.props.closeEditContactDialog():a.props.closeNewContactDialog()},a}return Object(l.a)(t,e),Object(c.a)(t,[{key:"componentDidUpdate",value:function(e,t,a){!e.contactDialog.props.open&&this.props.contactDialog.props.open&&("edit"===this.props.contactDialog.type&&this.props.contactDialog.data&&!f.a.isEqual(this.props.contactDialog.data,t)&&this.setState(Object(ie.a)({},this.props.contactDialog.data)),"new"!==this.props.contactDialog.type||f.a.isEqual(se,t)||this.setState(Object(ie.a)({},se)))}},{key:"canBeSubmitted",value:function(){return this.state.name.length>0}},{key:"render",value:function(){var e=this,t=this.props,a=t.contactDialog,n=t.addContact,c=t.updateContact,r=t.removeContact;return s.a.createElement(E.j,Object.assign({classes:{paper:"m-24"}},a.props,{onClose:this.closeComposeDialog,fullWidth:!0,maxWidth:"xs"}),s.a.createElement(E.a,{position:"static",elevation:1},s.a.createElement(E.Y,{className:"flex w-full"},s.a.createElement(E.ab,{variant:"subtitle1",color:"inherit"},"new"===a.type?"New Contact":"Edit Contact")),s.a.createElement("div",{className:"flex flex-col items-center justify-center pb-24"},s.a.createElement(E.b,{className:"w-96 h-96",alt:"contact avatar",src:this.state.avatar}),"edit"===a.type&&s.a.createElement(E.ab,{variant:"h6",color:"inherit",className:"pt-8"},this.state.name))),s.a.createElement(E.l,{classes:{root:"p-24"}},s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"account_circle")),s.a.createElement(E.X,{className:"mb-24",label:"Name",autoFocus:!0,id:"name",name:"name",value:this.state.name,onChange:this.handleChange,variant:"outlined",required:!0,fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"}),s.a.createElement(E.X,{className:"mb-24",label:"Last name",id:"lastName",name:"lastName",value:this.state.lastName,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"star")),s.a.createElement(E.X,{className:"mb-24",label:"Nickname",id:"nickname",name:"nickname",value:this.state.nickname,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"phone")),s.a.createElement(E.X,{className:"mb-24",label:"Phone",id:"phone",name:"phone",value:this.state.phone,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"email")),s.a.createElement(E.X,{className:"mb-24",label:"Email",id:"email",name:"email",value:this.state.email,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"domain")),s.a.createElement(E.X,{className:"mb-24",label:"Company",id:"company",name:"company",value:this.state.company,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"work")),s.a.createElement(E.X,{className:"mb-24",label:"Job title",id:"jobTitle",name:"jobTitle",value:this.state.jobTitle,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"cake")),s.a.createElement(E.X,{className:"mb-24",id:"birthday",label:"Birthday",type:"date",value:this.state.birthday,onChange:this.handleChange,InputLabelProps:{shrink:!0},variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"home")),s.a.createElement(E.X,{className:"mb-24",label:"Address",id:"address",name:"address",value:this.state.address,onChange:this.handleChange,variant:"outlined",fullWidth:!0})),s.a.createElement("div",{className:"flex"},s.a.createElement("div",{className:"min-w-48 pt-20"},s.a.createElement(E.w,{color:"action"},"note")),s.a.createElement(E.X,{className:"mb-24",label:"Notes",id:"notes",name:"notes",value:this.state.notes,onChange:this.handleChange,variant:"outlined",multiline:!0,rows:5,fullWidth:!0}))),"new"===a.type?s.a.createElement(E.k,{className:"justify-between pl-16"},s.a.createElement(E.c,{variant:"contained",color:"primary",onClick:function(){n(e.state),e.closeComposeDialog()},disabled:!this.canBeSubmitted()},"Add")):s.a.createElement(E.k,{className:"justify-between pl-16"},s.a.createElement(E.c,{variant:"contained",color:"primary",onClick:function(){c(e.state),e.closeComposeDialog()},disabled:!this.canBeSubmitted()},"Save"),s.a.createElement(E.x,{onClick:function(){r(e.state.id),e.closeComposeDialog()}},s.a.createElement(E.w,null,"delete"))))}}]),t}(i.Component);Object(h.b)(function(e){return{contactDialog:e.friendsApp.contacts.contactDialog}},function(e){return Object(d.c)({closeEditContactDialog:V,closeNewContactDialog:z,addContact:Z,updateContact:$,removeContact:ee},e)})(ue);var me=a(24),de={entities:[],page:{},totalPage:"",searchText:"",selectedContactIds:[],routeParams:{},contactDialog:{type:"new",props:{open:!1},data:null},confirmDialog:{props:{open:!1},user_id:null}},pe=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:de,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case y:return Object(ie.a)({},e,{entities:t.payload,routeParams:t.routeParams,page:t.params,totalPage:t.totalPage});case A:return Object(ie.a)({},e,{searchText:t.searchText});case P:var a=t.contactId,n=Object(me.a)(e.selectedContactIds);return n=void 0!==n.find(function(e){return e===a})?n.filter(function(e){return e!==a}):Object(me.a)(n).concat([a]),Object(ie.a)({},e,{selectedContactIds:n});case S:var c=Object.keys(e.entities).map(function(t){return e.entities[t]}).map(function(e){return e.id});return Object(ie.a)({},e,{selectedContactIds:c});case j:return Object(ie.a)({},e,{selectedContactIds:[]});case D:return Object(ie.a)({},e,{contactDialog:{type:"new",props:{open:!0},data:null}});case w:return Object(ie.a)({},e,{contactDialog:{type:"new",props:{open:!1},data:null}});case I:return Object(ie.a)({},e,{contactDialog:{type:"edit",props:{open:!0},data:t.data}});case k:return Object(ie.a)({},e,{contactDialog:{type:"edit",props:{open:!1},data:null}});case U:return Object(ie.a)({},e,{confirmDialog:{props:{open:!0},user_id:t.data}});case H:return Object(ie.a)({},e,{confirmDialog:{props:{open:!1},user_id:null}});default:return e}},he=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case O:return t.payload;default:return e}},Ce=Object(d.d)({contacts:pe,user:he}),fe=a(65),Ee=a.n(fe),ge=a(249),be=a.n(ge),ve=a(250),Oe=a.n(ve),Ne=a(251),Te=a.n(Ne),ye=a(253),Ae=a.n(ye),Pe=a(252),Se=a.n(Pe),je=function(e){function t(){var e,a;Object(n.a)(this,t);for(var c=arguments.length,l=new Array(c),i=0;i<c;i++)l[i]=arguments[i];return(a=Object(r.a)(this,(e=Object(o.a)(t)).call.apply(e,[this].concat(l)))).state={open:!1},a.handleClickOpen=function(){a.setState({open:!0})},a.handleClose=function(){a.setState({open:!1})},a.removeContact=function(e){var t=localStorage.getItem("item_id");v.a.delete(T.a.baseUrl+"/admin/users/"+t+"/friends/"+e+"/").then(function(e){return a.ReturnMainPage()})},a.ReturnMainPage=function(){var e=a.props,t=e.history,n=e.page;t.push({pathname:"/app/pages/profile",page:n}),a.props.closeConfirmDialog()},a}return Object(l.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){var e=this,t=this.props,a=t.closeConfirmDialog,n=t.confirmDialog;return s.a.createElement(be.a,{open:n.props.open,onClose:this.handleClose,"aria-labelledby":"alert-dialog-title","aria-describedby":"alert-dialog-description"},s.a.createElement(Se.a,{id:"alert-dialog-title"},"Permanently delete?"),s.a.createElement(Te.a,null,s.a.createElement(Ae.a,{id:"alert-dialog-description"},"Please note that it will delete all the user data.")),s.a.createElement(Oe.a,null,s.a.createElement(Ee.a,{onClick:function(){e.removeContact(n.user_id)},color:"primary"},"Agree"),s.a.createElement(Ee.a,{onClick:function(){a()},color:"primary",autoFocus:!0},"Disagree")))}}]),t}(s.a.Component);var De=Object(h.b)(function(e){var t=e.friendsApp;return{confirmDialog:t.contacts.confirmDialog,page:t.contacts.page}},function(e){return Object(d.c)({closeEditContactDialog:V,closeNewContactDialog:z,addContact:Z,updateContact:$,removeContact:ee,closeConfirmDialog:Q},e)})(je),we=function(e){function t(){return Object(n.a)(this,t),Object(r.a)(this,Object(o.a)(t).apply(this,arguments))}return Object(l.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=localStorage.getItem("item_id");this.props.getContacts(e),this.props.getUserData()}},{key:"componentDidUpdate",value:function(e,t){if(!f.a.isEqual(this.props.location,e.location)){var a=localStorage.getItem("item_id");this.props.getContacts(a)}}},{key:"render",value:function(){var e=this;return s.a.createElement(s.a.Fragment,null,s.a.createElement(m.m,{classes:{contentCardWrapper:"p-16 sm:p-24 pb-80",leftSidebar:"w-256 border-0",header:"min-h-72 h-72 sm:h-136 sm:min-h-136"},content:s.a.createElement(le,null),sidebarInner:!0,onRef:function(t){e.pageLayout=t},innerScroll:!0}),s.a.createElement(De,{history:this.props.history}))}}]),t}(i.Component);t.default=Object(C.a)("friendsApp",Ce)(Object(u.withStyles)(function(e){return{addButton:{position:"absolute",right:12,bottom:12,zIndex:99}}},{withTheme:!0})(Object(p.g)(Object(h.b)(function(e){var t=e.friendsApp;return{contacts:t.contacts.entities,selectedContactIds:t.contacts.selectedContactIds,searchText:t.contacts.searchText,user:t.user}},function(e){return Object(d.c)({getContacts:F,getUserData:N,openNewContactDialog:J},e)})(we))))}}]);