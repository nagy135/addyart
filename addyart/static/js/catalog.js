$(document).ready(function(){
    $('#category-select').change(function(e){
        var chosen = $('#category-select option:selected')[0].value;
        showCategoryN(chosen, 5);
    });
    var lazyLoadInstance = new LazyLoad({
        elements_selector: ".lazy"
        // ... more custom settings?
    });
    showCategoryN("", 5);
});

function showCategoryN(category, n){
    console.log("category", category);
    var sections = $('.page-section');
    sections.hide();
    sections.each(function(i){
        console.log($(this).attr('data-category'));
        if (  n > 0 ){
            if ( category != ""  ){
                if ( $(this).attr('data-category') == category ){
                    $(this).show();
                    n = n - 1;
                }
            } else {
                $(this).show();
                n = n - 1;
            }
        }
    });
}
