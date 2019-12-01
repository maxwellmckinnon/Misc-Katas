function largestRange(array) {
	console.log("\n\n-------------------\nNew Case\n-------------------\n:");
	
	var dict = new Object();
	var largestrange = 0;
	var indexlargestrange = 0;
	console.log(array);
  for (i = 0; i < array.length; i++){
		// If we hit a number we've already hit, toss it out, no need for it!
		if (array[i] in dict) { continue; }
			
		console.log("Start i=%s, val=%s, dict: %o", i, array[i], dict);
		dict[array[i]] = [array[i]];
		if (array[i]-1 in dict){
			console.log("Pre-run found at i=%s", i)
			var minValFromLowerArrayRange = dict[array[i]-1][0];
			console.log("minValFromLowerArrayRange: %s", minValFromLowerArrayRange);
			dict[minValFromLowerArrayRange] = dict[minValFromLowerArrayRange].concat([array[i]]);
			console.log("Concat: \n - %o with \n - %o", dict[minValFromLowerArrayRange], [array[i]]);
			dict[array[i]] = dict[minValFromLowerArrayRange];
			console.log("Concat results: %o", dict);
		}
		
		if (array[i]+1 in dict){
			console.log("Post-run found at i=%s", i);
			var higherArrayRange = dict[array[i]+1];
			var maxValFromHigherArrayRange = higherArrayRange[higherArrayRange.length - 1];
			dict[maxValFromHigherArrayRange] = dict[array[i]].concat(dict[maxValFromHigherArrayRange]);
			dict[array[i]] = dict[maxValFromHigherArrayRange];
			if (array[i]-1 in dict){
				var minValFromLowerArrayRange = dict[array[i]-1][0];
				dict[minValFromLowerArrayRange] = dict[array[i]];
				console.log("Post-run and pre-run combined: %s", dict[array[i]-1]);
			}
		}
		
		if (dict[array[i]].length > largestrange){
			indexlargestrange = array[i];
			largestrange = dict[array[i]].length;
			// console.log("New largest range found at i=%s, rangelength=%s", i, largestrange);
			// console.log("Largest array: %s", dict[array[i]]);
		}
		
		console.log("i=%s, dict: %o", i, dict);
		
	}
	console.log("Final dict found: %0", dict);
	console.log(dict[indexlargestrange]);
	var length = dict[indexlargestrange].length;
	console.log("Answer: %o", [dict[indexlargestrange][0], dict[indexlargestrange][length - 1]]);
	return [dict[indexlargestrange][0], dict[indexlargestrange][length - 1]];
}

// Do not edit the line below.
exports.largestRange = largestRange;

