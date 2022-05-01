using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RefreshRate : MonoBehaviour {
    public GameObject b1;
    public GameObject b2;
    public GameObject b3;
    public GameObject b4;
    public GameObject b5;
    public GameObject b6;

    void Start() {
      StartCoroutine(Coroutine7_5());
      StartCoroutine(Coroutine15());
      StartCoroutine(Coroutine30());
      StartCoroutine(Coroutine60());
      StartCoroutine(Coroutine120());
      StartCoroutine(Coroutine240());
    }

    IEnumerator Coroutine7_5() {
      float t = 7.5f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b4.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b4.transform.position.y, b4.transform.position.z);
      }
    }

    IEnumerator Coroutine15() {
      float t = 15f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b3.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b3.transform.position.y, b3.transform.position.z);
      }
    }

    IEnumerator Coroutine30() {
      float t = 30f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b2.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b2.transform.position.y, b2.transform.position.z);
      }
    }

    IEnumerator Coroutine60() {
      float t = 60f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b1.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b1.transform.position.y, b1.transform.position.z);
      }
    }

    IEnumerator Coroutine120() {
      float t = 120f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b5.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b5.transform.position.y, b5.transform.position.z);
      }
    }

    IEnumerator Coroutine240() {
      float t = 240f;
      while(true) {
        yield return new WaitForSeconds(1f/t);
        b6.transform.position = new Vector3(-16.109f - 2.5f*(Time.time % 1), b6.transform.position.y, b6.transform.position.z);
      }
    }
}
