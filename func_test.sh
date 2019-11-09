test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Basic functional tests
run test_hash python insert_key_values_pairs.py hash sorted.txt 10
assert_no_stderr
assert_exit_code 0

run test_avl python insert_key_values_pairs.py avl sorted.txt 10
assert_no_stderr
assert_exit_code 0

run test_bst python insert_key_values_pairs.py tree sorted.txt 10
assert_no_stderr
assert_exit_code 0
