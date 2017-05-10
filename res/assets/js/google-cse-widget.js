define(['assetman'], function (assetman) {
    window.__gcse = {
        parseTags: 'explicit',
        callback: function () {
            google.search.cse.element.go();
        }
    };

    return function (widget) {
        assetman.loadJS('https://cse.google.com/cse.js?cx=' + widget.em.data('cx'));
    }
});
