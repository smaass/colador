from unittest import TestCase

from colador.messages_group import MessagesGroup


class MessagesGroupTestCase(TestCase):

    def test_iteration(self):

        some_messages = ['a', 'b', 'c', 'd']
        group = MessagesGroup(None, some_messages)

        for i, message in enumerate(group):
            self.assertEqual(some_messages[i], message)

    def test_addition(self):

        msgs1 = ['a', 'b']
        msgs2 = ['c', 'd', 'e']
        group1 = MessagesGroup(1, msgs1)
        group2 = MessagesGroup(2, msgs2)

        sum_group = group1 + group2
        self.assertSequenceEqual(sum_group.messages, msgs1 + msgs2)
        self.assertEqual(sum_group.colador, group1.colador)

        sum_group_inv = group2 + group1
        self.assertSequenceEqual(sum_group_inv.messages, msgs2 + msgs1)
        self.assertEqual(sum_group_inv.colador, group2.colador)

    def test_len(self):

        msgs = ['a', 'b', 'c', 'd', 'e']
        group = MessagesGroup(None, msgs)
        self.assertEqual(len(msgs), len(group))
