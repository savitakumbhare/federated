# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for intrinsic_utils.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
import tensorflow as tf

from tensorflow_federated.python.core.impl import context_stack_impl
from tensorflow_federated.python.core.impl import intrinsic_utils


class IntrinsicUtilsTest(absltest.TestCase):

  def test_zero_for(self):
    self.assertEqual(
        str(
            intrinsic_utils.zero_for(
                tf.int32, context_stack_impl.context_stack).type_signature),
        'int32')

  def test_plus_for(self):
    self.assertEqual(
        str(
            intrinsic_utils.plus_for(
                tf.int32, context_stack_impl.context_stack).type_signature),
        '(<int32,int32> -> int32)')


if __name__ == '__main__':
  absltest.main()
