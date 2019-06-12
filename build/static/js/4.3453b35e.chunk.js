(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{1827:function(e,t,a){"use strict";a.r(t);var n=a(16),r=a(7),s=a(8),i=a(13),l=a(12),o=a(14),c=a(0),m=a.n(c),u=a(1),d=a(45),p=a(119),f=a(10),b=a(4),h=a.n(b),E=a(27),v=a(92),g=a.n(v),w=a(22),y=a(93),N=a(40),x=a(56),j=function(e){function t(){var e,a;Object(r.a)(this,t);for(var n=arguments.length,s=new Array(n),o=0;o<n;o++)s[o]=arguments[o];return(a=Object(i.a)(this,(e=Object(l.a)(t)).call.apply(e,[this].concat(s)))).state={canSubmit:!1},a.form=m.a.createRef(),a.disableButton=function(){a.setState({canSubmit:!1})},a.enableButton=function(){a.setState({canSubmit:!0})},a.onSubmit=function(e){a.props.submitRegister(e)},a}return Object(o.a)(t,e),Object(s.a)(t,[{key:"componentDidUpdate",value:function(e,t){return this.props.register.error&&(this.props.register.error.username||this.props.register.error.password||this.props.register.error.email)&&(this.form.updateInputsWithError(Object(n.a)({},this.props.register.error)),this.props.register.error=null,this.disableButton()),null}},{key:"render",value:function(){var e=this,t=this.state.canSubmit;return m.a.createElement("div",{className:"w-full"},m.a.createElement(g.a,{onValidSubmit:this.onSubmit,onValid:this.enableButton,onInvalid:this.disableButton,ref:function(t){return e.form=t},className:"flex flex-col justify-center w-full"},m.a.createElement(f.u,{className:"mb-16",type:"text",name:"displayName",label:"Display name",validations:{minLength:4},validationErrors:{minLength:"Min character length is 4"},InputProps:{endAdornment:m.a.createElement(u.z,{position:"end"},m.a.createElement(u.w,{className:"text-20",color:"action"},"person"))},variant:"outlined",required:!0}),m.a.createElement(f.u,{className:"mb-16",type:"text",name:"email",label:"Email",validations:"isEmail",validationErrors:{isEmail:"Please enter a valid email"},InputProps:{endAdornment:m.a.createElement(u.z,{position:"end"},m.a.createElement(u.w,{className:"text-20",color:"action"},"email"))},variant:"outlined",required:!0}),m.a.createElement(f.u,{className:"mb-16",type:"password",name:"password",label:"Password",validations:"equalsField:confirmpassword",validationErrors:{equalsField:"Passwords do not match"},InputProps:{endAdornment:m.a.createElement(u.z,{position:"end"},m.a.createElement(u.w,{className:"text-20",color:"action"},"vpn_key"))},variant:"outlined",required:!0}),m.a.createElement(f.u,{className:"mb-16",type:"password",name:"confirmpassword",label:"Confirm Password",validations:"equalsField:password",validationErrors:{equalsField:"Passwords do not match"},InputProps:{endAdornment:m.a.createElement(u.z,{position:"end"},m.a.createElement(u.w,{className:"text-20",color:"action"},"vpn_key"))},variant:"outlined",required:!0}),m.a.createElement(u.c,{type:"submit",variant:"contained",color:"primary",className:"w-full mx-auto mt-16 normal-case","aria-label":"REGISTER",disabled:!t,value:"legacy"},"Register")))}}]),t}(c.Component);var O=Object(y.g)(Object(N.a)(function(e){var t=e.auth;return{register:t.register,user:t.user}},function(e){return Object(w.c)({submitRegister:x.n},e)})(j)),C=a(6),k=function(e){function t(){var e,a;Object(r.a)(this,t);for(var s=arguments.length,o=new Array(s),c=0;c<s;c++)o[c]=arguments[c];return(a=Object(i.a)(this,(e=Object(l.a)(t)).call.apply(e,[this].concat(o)))).state={name:"",email:"",password:"",passwordConfirm:"",acceptTermsConditions:!1},a.handleChange=function(e){a.setState(C.a.set(Object(n.a)({},a.state),e.target.name,"checkbox"===e.target.type?e.target.checked:e.target.value))},a}return Object(o.a)(t,e),Object(s.a)(t,[{key:"canBeSubmitted",value:function(){var e=this.state,t=e.email,a=e.password,n=e.passwordConfirm,r=e.acceptTermsConditions;return t.length>0&&a.length>0&&a.length>3&&a===n&&r}},{key:"render",value:function(){var e=this.props.classes,t=this.state.acceptTermsConditions;return m.a.createElement("div",{className:h()(e.root,"flex flex-col flex-auto flex-no-shrink items-center justify-center p-32")},m.a.createElement("div",{className:"flex flex-col items-center justify-center w-full"},m.a.createElement(f.b,{animation:"transition.expandIn"},m.a.createElement(u.d,{className:"w-full max-w-384"},m.a.createElement(u.e,{className:"flex flex-col items-center justify-center p-32"},m.a.createElement("img",{className:"w-128 m-32",src:"assets/images/logos/fuse.svg",alt:"logo"}),m.a.createElement(u.ab,{variant:"h6",className:"mt-16 mb-32"},"CREATE AN ACCOUNT"),m.a.createElement(O,null),m.a.createElement(u.q,{className:"items-center"},m.a.createElement(u.r,{control:m.a.createElement(u.f,{name:"acceptTermsConditions",checked:t,onChange:this.handleChange}),label:"I read and accept terms and conditions"})),m.a.createElement(u.c,{variant:"contained",color:"primary",className:"w-224 mx-auto mt-16","aria-label":"Register",disabled:!this.canBeSubmitted()},"CREATE AN ACCOUNT"),m.a.createElement("div",{className:"flex flex-col items-center justify-center pt-32 pb-24"},m.a.createElement("span",{className:"font-medium"},"Already have an account?"),m.a.createElement(E.a,{className:"font-medium",to:"/pages/auth/login"},"Login")))))))}}]),t}(c.Component);t.default=Object(d.withStyles)(function(e){return{root:{background:"radial-gradient("+Object(p.darken)(e.palette.primary.dark,.5)+" 0%, "+e.palette.primary.dark+" 80%)",color:e.palette.primary.contrastText}}},{withTheme:!0})(k)}}]);