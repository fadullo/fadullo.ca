(function () {
  var root = document.documentElement;
  var toggle = document.querySelector('[data-drawer-toggle]');
  var backdrop = document.querySelector('.drawer-backdrop');
  if (!toggle) return;

  var KEY = 'drawer-open';

  function isOpen() {
    return root.classList.contains('drawer-open');
  }

  function setOpen(open) {
    root.classList.toggle('drawer-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    try { localStorage.setItem(KEY, open ? '1' : '0'); } catch (e) {}
  }

  toggle.setAttribute('aria-expanded', isOpen() ? 'true' : 'false');

  toggle.addEventListener('click', function () {
    setOpen(!isOpen());
  });

  if (backdrop) {
    backdrop.addEventListener('click', function () {
      setOpen(false);
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen()) {
      setOpen(false);
      toggle.focus();
    }
  });
})();
