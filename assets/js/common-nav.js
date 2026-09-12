(function(){
  const btn=document.querySelector('.sc-global-menu');
  const links=document.querySelector('.sc-global-links');
  if(btn&&links){btn.addEventListener('click',()=>{const open=links.classList.toggle('open');btn.setAttribute('aria-expanded',String(open));});
    links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{links.classList.remove('open');btn.setAttribute('aria-expanded','false')}));}
})();
