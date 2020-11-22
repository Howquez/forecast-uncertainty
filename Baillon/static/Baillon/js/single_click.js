// Thank you snunnari. The single switching point script is copied (and slightly adjusted) from this repo
// https://github.com/snunnari/otree_psm)

// :not('.demonstration')

console.log("engines running");
var switchingValue;

$(document).ready(function () {
    $("input[type=radio]:not(.demonstration)").change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;
            var strictlyAfterClickedRadio = false;
            var before = []

            var radios = document.querySelectorAll("input[type=radio]:not(.demonstration)");

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                // mark radios that follow (and include) the clickedRadio
                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    continue;
                }

                // mark radios that follow the clickedRadio
                if (radios[i-1] === clickedRadio) {
                    strictlyAfterClickedRadio = true;
                    continue;
                }

                // if clickedRadio is A, check all following radios as B
                if (strictlyAfterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B') {
                    radio.checked = true;
                }
                // if clickedRadio is A, check that and all previous radios as A
                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }
                // if clickedRadio is B, check that and all following radios as B
                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }
                // legacy: enable previously disabled radios
                // radio.removeAttribute("disabled")
            }

            // generate array containing radios previous to clickedRadio
            for (j = 0; j < radios.length; ++j) {
                before.push(j);
                var radio = radios[j]
                    if (radio === clickedRadio) {
                        break;
                    }
            }

            // if clickedRadio is B, check all previous radios as A
            for (k = 0; k < before.length - 2; ++k) {
                var radio = radios[k];

                if (clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }
            }

            // output the switching point
            var switchingRadioIndex = Math.ceil(before.length/2);
            var switchingPoint = document.getElementsByName("choice_".concat(switchingRadioIndex))[1];
            switchingValue = switchingPoint.id;
            console.log(switchingValue);

        }
    );
});