

// function poker(allHands) {
//     return allMax()
// }
// =======================
// Sorts cards by rank
function card_ranks(hand) {
	let rank = '--23456789TJQKA'.split('');
	return hand.map((h) => Number(rank.indexOf(h[0]))).sort((a,b) => a - b).reverse()
}

function hand_rank(hand) {
	let ranked = card_ranks(hand);

	// Straight Flush: straight and flush
	if(straight(ranked) && flush(hand)) {
		return 8

	// Four of a Kind: 
	} else if(kind(ranked,4)) {
		return 7

	// Full House
	} else if(kind(ranked, 3) && kind(ranked, 2)) {
		return 6
	
	// Flush
	} else if(flush(hand)) {
		return 5;
	
	// Straight
	} else if(straight(ranked)) {
		return 4;

	// Three of a Kind
	} else if(kind(ranked, 3)) {
		return 3;

	// Two Pair
	} else if(two_pair(ranked)) {
		return 2;
	
	// Pair
	} else if(kind(ranked, 2)) {
		return 1;
	
	// High Card
	} else {
		return 0
	}
}

function flush(hand) {
	let suits = hand.reduce((acc, item) => {
		if(acc.hasOwnProperty(item[1])) {
			acc[item[1]]++
		} else {
			acc[item[1]] = 1
		}
		return acc;
	}, {})
	return Object.keys(suits).length === 1
}

function straight(hand) {
	return Math.max(...hand) - Math.min(...hand) === 4 && (new Set(hand)).size === 5;
}

function kind(hand, n) {
	let obj = {};
	let answer = false;
	
	
	hand.map((card) => {
		if(obj[card]) {
			obj[card]++
		} else {
			obj[card] = 1;
		}
	})

	let i = 0;
	let run = true;
	while(i < hand.length && run) {
		let count = obj[hand[i]]
		if(count === n) {
			run = false;
			answer = hand[i];
		}
		i++
	}
	return answer;
	
	
	// let last = hand[0];
	// let count = 1;
	// let answer = null;
	// for(let i = 1; i < hand.length; i++) {
	// 	if(hand[i] === last) {
	// 		count++
	// 		answer = last;
	// 	} else {
	// 		if(count === n) {
	// 			return answer;
	// 		}
	// 		last = hand[i]
	// 	}
	// }
	// return count === n ? answer : false;
}

function two_pair(hand) {
	let p1 = kind(hand, 2);
	let p2 = kind(hand.reverse(), 2);
	console.log(p1, p2)
	return (p1 && p2) && (p1 !== p2) ? [p1, p2] : false;
}

function tests() {
	let c1 = 'AH KC QD JS TC'.split(' ');
	let c2 = 'AH KH QH JH TH'.split(' ');
	let c3 = '5S 9S 2S TS KS'.split(' ');
	let c4 = '5S 5H 5D 4D 3D'.split(' ');
	let c5 = '5S 5H 4D 4C AH'.split(' ');
	let c6 = '5C 5D 5H 5S AS'.split(' ');
	let r1 = card_ranks(c1);
	let r2 = card_ranks(c2);
	let r3 = card_ranks(c3);
	let r4 = card_ranks(c4);
	let r5 = card_ranks(c5);
	let r6 = card_ranks(c6);
	console.log(hand_rank(r6))
	console.log(two_pair(r5))
	return;

	// console.log(hand_rank(c1))
	// console.log('**********************************')
	// console.log('Straight')
	// console.assert(straight(r1), {hand: r1, message: "Correctly identifies a straight"})
	// console.assert(!straight(r3), "Failed to identify as a non-straight")
	// console.log('**********************************')
	// console.log('Flush')
	// console.assert(flush(c3),"Not a flush")
	// console.assert(!flush(c1),"Not a flush")
	// console.log('**********************************')
	// console.log('Kind')
	// console.log(kind(r4, 4))
	// console.log(two_pair(r4))
	let stats = {percentages: {}}
	let iterations = 100000;
	for(let i = 0; i < iterations; i++) {
		let hand = handGenerator();
		let rank = hand_rank(hand)
		if(stats[rank]) {
			stats[rank]++
		} else {
			stats[rank] = 1;
		}
		// console.log(`${rank}:`, hand)
	}
	for(let prop in stats) {
		stats.percentages[prop] = (stats[prop]/iterations * 100).toFixed(2) + '%'
	}
	console.log(stats);
	


}

function handGenerator() {
	let suits = 'CDHS'
	let values = '23456789TJQKA'
	let cards = [];
	for(let i = 0; i < suits.length; i++) {
		for(let j = 0; j < values.length; j++) {
			cards.push(values[j] + suits[i]);
		}
	}
	let shuffled = shuffle(cards)
	let hand = shuffled.slice(0, 5)
	return hand;
}

function shuffle(original) {
	let array = [...original]
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i

    // swap elements array[i] and array[j]
    // we use "destructuring assignment" syntax to achieve that
    // you'll find more details about that syntax in later chapters
    // same can be written as:
    // let t = array[i]; array[i] = array[j]; array[j] = t
    [array[i], array[j]] = [array[j], array[i]];
	}
	
	return array;
}

tests();