using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;

public class Measurement : MonoBehaviour {
  public GameObject CameraOffset;
  public GameObject MainCamera;
  public GameObject LeftController;
  public GameObject RightController;
  public Camera XRCamera;
  float lastUpdate;
  Vector3 leftControllerPos;
  Vector3 rightControllerPos;
  float lastRefresh;
  Ping ping1;
  Ping ping2;
  Ping ping3;
  Ping ping4;
  Ping ping5;

  void Start() {
    lastUpdate = Time.time;
    leftControllerPos = LeftController.transform.localPosition;
    rightControllerPos = RightController.transform.localPosition;

    // Get ping time
    ping1 = new Ping("52.219.116.88");  // us-west-1 - north california
    ping2 = new Ping("52.218.225.128"); // us-west-2 - oregon
    ping3 = new Ping("52.217.164.24");  // us-east-1 - north virginia
    ping4 = new Ping("52.219.107.9");   // us-east-2 - ohio
    ping5 = new Ping("52.95.146.225");  // ca-central-1	- central canada

    StartCoroutine (PingUpdate());
  }

  IEnumerator PingUpdate() {
      yield return new WaitForSeconds (1f);
      if (ping1.isDone && ping2.isDone && ping3.isDone && ping4.isDone && ping5.isDone) {
        print("us-west-1: " + ping1.time);
        print("us-west-2: " + ping2.time);
        print("us-east-1: " + ping3.time);
        print("us-east-2: " + ping4.time);
        print("ca-central-1: " + ping5.time);
      } else {
        StartCoroutine (PingUpdate ());
      }
  }

  void Update() {
    // resolution
    // print("w: " + XRCamera.pixelWidth);
    // print("h: " + XRCamera.pixelHeight);

    // refresh rate
    // float delta = Time.time - lastRefresh;
    // float rate = 1f / delta;
    // print("Refresh Rate: " + rate);
    // lastRefresh = Time.time;

    // tracking rate
    // if (!(leftControllerPos.Equals(LeftController.transform.localPosition) && rightControllerPos.Equals(RightController.transform.localPosition))) {
    //   float delta = Time.time - lastUpdate;
    //   float rate = 1f / delta;
    //
    //   print("Tracking Rate: " + rate);
    //
    //   leftControllerPos = LeftController.transform.localPosition;
    //   rightControllerPos = RightController.transform.localPosition;
    //   lastUpdate = Time.time;
    // }

    // height
    // print("Height: " + MainCamera.transform.localPosition.y);

    // wingspan
    // print("Wingspan: " + Vector3.Distance(LeftController.transform.localPosition, RightController.transform.localPosition));

    // room size
    // print("Position x: " + MainCamera.transform.localPosition.x);
    // print("Position z: " + MainCamera.transform.localPosition.z);

    // IPD
    // print("IPD: " + XRCamera.stereoSeparation);
    // Matrix4x4 leftMatrix = XRCamera.GetStereoViewMatrix(Camera.StereoscopicEye.Left);
    // Matrix4x4 rightMatrix = XRCamera.GetStereoViewMatrix(Camera.StereoscopicEye.Right);
    // print(leftMatrix);
    // print(rightMatrix);

    // Vector3 leftEye = UnityEngine.XR.InputTracking.GetLocalPosition(UnityEngine.XR.XRNode.LeftEye);
    // Vector3 rightEye = UnityEngine.XR.InputTracking.GetLocalPosition(UnityEngine.XR.XRNode.RightEye);
    // print("IPD: " + Vector3.Distance(leftEye, rightEye));
  }
}
