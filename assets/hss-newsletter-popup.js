(function () {
  var DISMISSED_KEY = 'hss-newsletter-popup-dismissed-at';
  var SUBSCRIBED_KEY = 'hss-newsletter-popup-subscribed';

  function safeGet(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function safeSet(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (error) {
      /* localStorage unavailable (private mode, disabled storage, etc.) — fail silently */
    }
  }

  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  ready(function () {
    document.querySelectorAll('.hss-newsletter-popup').forEach(function (modal) {
      var closeButton = modal.querySelector('[id^="ModalClose-"]');
      if (closeButton) {
        closeButton.addEventListener('click', function () {
          safeSet(DISMISSED_KEY, String(Date.now()));
        });
      }

      var justSubscribed = !!modal.querySelector('[data-newsletter-success]');
      if (justSubscribed) {
        safeSet(SUBSCRIBED_KEY, '1');
        window.setTimeout(function () {
          if (typeof modal.show === 'function') modal.show();
        }, 300);
        return;
      }

      if (safeGet(SUBSCRIBED_KEY)) return;

      var dismissedAt = safeGet(DISMISSED_KEY);
      if (dismissedAt) {
        var reappearDays = parseFloat(modal.dataset.reappearDays);
        if (isNaN(reappearDays)) reappearDays = 7;
        var elapsedDays = (Date.now() - parseInt(dismissedAt, 10)) / 86400000;
        if (elapsedDays < reappearDays) return;
      }

      var delaySeconds = parseFloat(modal.dataset.delay);
      if (isNaN(delaySeconds)) delaySeconds = 6;

      window.setTimeout(function () {
        if (typeof modal.show === 'function') modal.show();
      }, delaySeconds * 1000);
    });
  });
})();
