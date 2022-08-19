const rangeInput = document.querySelectorAll('.range-input input'),
      progress = document.querySelector('.slider .progress'),
      priceInput = document.querySelectorAll('.price-input .field input');

let priceGap = 10;

priceInput.forEach(input => {
    input.addEventListener('input', e =>{
        let minVal = parseInt(priceInput[0].value),
            maxVal = parseInt(priceInput[1].value);
        // if(maxVal > rangeInput[1].max){
        //     priceInput[1].value = rangeInput[1].max;
        //     maxVal = rangeInput[1].max;
        // } 
        // if(minVal < rangeInput[0].min) {
        //     priceInput[0].value = rangeInput[0].min;
        //     minVal = rangeInput[0].min;
        // }
        if((maxVal - minVal >= priceGap) && maxVal <= rangeInput[1].max){
            if(e.target.className === "input-min"){
                rangeInput[0].value = minVal;
                progress.style.left = ((minVal - rangeInput[0].min) / (rangeInput[0].max - rangeInput[0].min)) * 100 + "%";
            }else{
                rangeInput[1].value = maxVal;
                progress.style.right = 100 - ((maxVal - rangeInput[1].min) / (rangeInput[1].max - rangeInput[0].min)) * 100 + "%";
            }
        }
    })
})

rangeInput.forEach(input => {
    input.addEventListener('input', e =>{
        let minVal = parseInt(rangeInput[0].value),
            maxVal = parseInt(rangeInput[1].value);
        
        if(maxVal - minVal < priceGap){
            if(e.target.className === "range-min"){
                rangeInput[0].value = maxVal - priceGap;
            }else{
                rangeInput[1].value = minVal + priceGap;
            }
        }else{
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            progress.style.left = ((minVal - rangeInput[0].min) / (rangeInput[0].max - rangeInput[0].min)) * 100 + "%";
            // console.log('max : ' + rangeInput[0].max + ' | min : ' + rangeInput[0].min + ' | current : ' + minVal + ' | max-min : ' + (rangeInput[0].max - rangeInput[0].min) + ' | percentage : ' + (minVal / (parseInt(rangeInput[0].max) - parseInt(rangeInput[0].min))) * 100 + "%")
            progress.style.right = 100 - ((maxVal - rangeInput[1].min) / (rangeInput[1].max - rangeInput[0].min)) * 100 + "%";
        }
    })
})

