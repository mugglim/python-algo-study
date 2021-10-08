function solution(new_id) {
	const lv1Id = convertByLv1(new_id);
	const lv2Id = convertByLv2(lv1Id);
	const lv3Id = convertByLv3(lv2Id);
	const lv4Id = convertByLv4(lv3Id);
	const lv5Id = convertByLv5(lv4Id);
	const lv6Id = convertByLv6(lv5Id);
	const lv7Id = convertByLv7(lv6Id);
	return lv7Id;
}

function getStringMul(str, cnt) {
	return new Array(cnt).fill(str).join('');
}

function convertByLv1(new_id) {
	return new_id
		.split('')
		.map((el) => el.toLowerCase())
		.join('');
}

function convertByLv2(new_id) {
	return new_id.replace(/[^a-z|\d|_|.|-]/g, '');
}

function convertByLv3(new_id) {
	return new_id.replace(/\.{2,}/g, '.');
}

function convertByLv4(new_id) {
	return new_id.replace(/(^\.|\.$)/g, '');
}

function convertByLv5(new_id) {
	return new_id.length === 0 ? 'a' : new_id;
}

function convertByLv6(new_id) {
	return new_id.length < 16 ? new_id : new_id.substring(0, 15).replace(/\.$/, '');
}

function convertByLv7(new_id) {
	return new_id.length > 2 ? new_id : new_id + getStringMul(new_id.slice(-1), 3 - new_id.length);
}

console.log(convertByLv7('1'));
