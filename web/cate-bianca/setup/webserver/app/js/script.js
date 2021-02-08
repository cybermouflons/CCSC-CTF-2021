
//Contentafter animations
window.onscroll = function(){

    var content = document.getElementsByClassName("contentafter");
    
    
    for(var count = 0; count < content.length; count++){
    
        var element = content[count];
        var result = isAnyPartOfElementInViewport(element);
        if(result == true){
    
            content[count].classList.add("appearanimation");
        }
        else if(result == false){
            content[count].classList.remove("appearanimation");
    
        }
    }
    }
    
    
    
    
    function isAnyPartOfElementInViewport(el) {
    
    const rect = el.getBoundingClientRect();
    // DOMRect { x: 8, y: 8, width: 100, height: 100, top: 8, right: 108, bottom: 108, left: 8 }
    const windowHeight = (window.innerHeight || document.documentElement.clientHeight);
    const windowWidth = (window.innerWidth || document.documentElement.clientWidth);
    
    // http://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap
    const vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
    const horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);
    
    return (vertInView && horInView);
    
    }
