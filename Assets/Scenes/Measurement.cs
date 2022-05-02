using System.Collections;
using System.Collections.Generic;
using System.IO;
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
  StreamWriter writer;

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

    writer = new StreamWriter("Data/" + System.DateTime.Now.ToString("F").Replace(",", "").Replace(':', '-') + ".txt", true);

    StartCoroutine (PingUpdate());
  }

  IEnumerator PingUpdate() {
      yield return new WaitForSeconds (1f);
      if (ping1.isDone && ping2.isDone && ping3.isDone && ping4.isDone && ping5.isDone) {
        writer.WriteLine("us-west-1: " + ping1.time);
        writer.WriteLine("us-west-2: " + ping2.time);
        writer.WriteLine("us-east-1: " + ping3.time);
        writer.WriteLine("us-east-2: " + ping4.time);
        writer.WriteLine("ca-central-1: " + ping5.time);
        ping1 = new Ping("52.219.116.88");  // us-west-1 - north california
        ping2 = new Ping("52.218.225.128"); // us-west-2 - oregon
        ping3 = new Ping("52.217.164.24");  // us-east-1 - north virginia
        ping4 = new Ping("52.219.107.9");   // us-east-2 - ohio
        ping5 = new Ping("52.95.146.225");  // ca-central-1	- central canada

        // resolution
        writer.WriteLine("camera-w: " + XRCamera.pixelWidth);
        writer.WriteLine("camera-h: " + XRCamera.pixelHeight);

        // IPD
        Vector3 leftEye = UnityEngine.XR.InputTracking.GetLocalPosition(UnityEngine.XR.XRNode.LeftEye);
        Vector3 rightEye = UnityEngine.XR.InputTracking.GetLocalPosition(UnityEngine.XR.XRNode.RightEye);
        writer.WriteLine("ipd: " + Vector3.Distance(leftEye, rightEye));
      }
      writer.Close();
      writer = new StreamWriter("Data/" + System.DateTime.Now.ToString("F").Replace(",", "").Replace(':', '-') + ".txt", true);
      StartCoroutine (PingUpdate ());
  }

  void Update() {
    // refresh rate
    float delta = Time.time - lastRefresh;
    float rate = 1f / delta;
    writer.WriteLine("refresh-rate: " + rate);
    lastRefresh = Time.time;

    // tracking rate
    if (!(leftControllerPos.Equals(LeftController.transform.localPosition) && rightControllerPos.Equals(RightController.transform.localPosition))) {
      delta = Time.time - lastUpdate;
      rate = 1f / delta;

      writer.WriteLine("tracking-rate: " + rate);

      leftControllerPos = LeftController.transform.localPosition;
      rightControllerPos = RightController.transform.localPosition;
      lastUpdate = Time.time;
    }

    // height & room size
    writer.WriteLine("main-camera: " + MainCamera.transform.localPosition);

    // wingspan
    writer.WriteLine("left-controller: " + LeftController.transform.localPosition);
    writer.WriteLine("right-controller: " + RightController.transform.localPosition);
  }
}
