$(document).ready(function() {
  var footer_banner = $('#footer__banner');
  var footer_banner_header = $('#footer__banner__header');

  function showFooterBanner() {
    footer_banner.removeClass('footer__banner--hide');
  }

  function hideFooterBanner() {
    footer_banner.addClass('footer__banner--hide');
  }

  function toggleFooterBanner() {
    if (footer_banner.hasClass('footer__banner--hide')) {
      showFooterBanner();
    } else {
      hideFooterBanner();
    }
  }

  footer_banner_header.on('click', function() {
    toggleFooterBanner();
  });
})
